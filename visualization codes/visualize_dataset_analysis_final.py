import matplotlib.pyplot as plt
import os
import json
import pandas as pd


"This code is to get at a glance the BaleUAVision dataset analysis. " \

"Part 1: At first, a csv file is produced with one sheet per hay field and each sheet " \
"practically shoes the number of annotated hay bales per image" \
'Note that the last sheet in this csv (-Average- sheet) includes the average density ' \
"of hay bales presented in each field."

"Part 2: This part serves as a supplementary material from the visualazation " \
"perspective offering some insights about the dataset itself "


##############################
########## PART 1 ############
##############################

# Base directory where your hay field folders are located.
base_dir = r'E:\BaleUAVision\Annotated Data'
# Output Excel workbook path.
output_excel = r'E:\BaleUAVision\annotation_counts.xlsx'

# Dictionary to hold DataFrames per hay field (each will be a sheet in the Excel workbook)
sheet_dfs = {}
# List to hold average annotation counts per hay field.
average_list = []

# Get list of folders starting with "Hay bales"
folders = [folder for folder in os.listdir(base_dir) if folder.startswith("Hay bales")]
# This is to sort folders in natural numeric order (i.e., 1, 2, 3, ... 16)
sorted_folders = sorted(folders, key=lambda x: int(x.split(" ")[-1]))

for field_folder in sorted_folders:
    field_path = os.path.join(base_dir, field_folder)
    # Find the COCO JSON file,assuming its filename contains "COCO" and ends with '.json'
    coco_files = [f for f in os.listdir(field_path) if f.endswith('.json') and 'COCO' in f]
    if not coco_files:
        print(f"No COCO json file found in {field_folder}")
        continue

    coco_file = coco_files[0]
    coco_path = os.path.join(field_path, coco_file)

    with open(coco_path, 'r') as f:
        coco_data = json.load(f)

    #Build a mapping from image id (converted to start at 1) to file name from the "images" section.
    images_mapping = {int(img['id']) + 1: img['file_name'] for img in coco_data.get('images', [])}

    #Count annotations per image (each annotation is one hay bale).
    # converting image ids so they start from 1.
    ann_count = {}
    for ann in coco_data.get('annotations', []):
        new_id = int(ann['image_id']) + 1
        ann_count[new_id] = ann_count.get(new_id, 0) + 1

    #Build a list of rows for the fadaframe.
    rows = []
    for new_id, file_name in images_mapping.items():
        count = ann_count.get(new_id, 0)
        rows.append({'image_id': new_id, 'file_name': file_name, 'annotation_count': count})

    df = pd.DataFrame(rows)
    sheet_dfs[field_folder] = df

    #Calculate the average number of annotations for this hay field.
    avg_count = df['annotation_count'].mean() if not df.empty else 0
    average_list.append({'hay_field': field_folder, 'avg_annotation_count': avg_count})

#Create a dataframe for the average summary.
avg_df = pd.DataFrame(average_list)
#Ensure the average summary is sorted in the same natural order.
avg_df = avg_df.sort_values(by='hay_field', key=lambda col: col.map(lambda x: int(x.split(" ")[-1])))

#Write the data to an Excel workbook with one sheet per hay field and the "Average" sheet, where the latter
#provides the average density of hay bales presented in each field.
with pd.ExcelWriter(output_excel) as writer:
    for field_folder, df in sheet_dfs.items():
        # Sheet name is the folder name (e.g., "Hay bales 1", "Hay bales 2", etc.)
        df.to_excel(writer, sheet_name=field_folder, index=False)
    avg_df.to_excel(writer, sheet_name="Average", index=False)

print(f"Annotation counts and averages saved to {output_excel}")





##############################
########## PART 2 ############
##############################


# Path to the Excel workbook created earlier
excel_file = r'E:\BaleUAVision\annotation_counts.xlsx'

# Open the Excel workbook and get all sheet names
xls = pd.ExcelFile(excel_file)
all_sheets = xls.sheet_names

# Separate the "Average" sheet from the hay field sheets
sheet_names = [sheet for sheet in all_sheets if sheet != "Average"]

# Load the "Average" sheet for the summary bar chart
df_avg = pd.read_excel(xls, sheet_name="Average")
# Extract numeric order from the hay_field name to sort naturally (i.e. 1,2,...,16)
df_avg['order'] = df_avg['hay_field'].apply(lambda x: int(x.split(" ")[-1]))
df_avg = df_avg.sort_values('order')

# ---------------------------
# Figure 1: Bar Chart of Average Annotations per Hay Field
plt.figure(figsize=(10, 6))
plt.bar(df_avg['hay_field'], df_avg['avg_annotation_count'], color='skyblue')
plt.xlabel('Hay Field')
plt.ylabel('Average Annotations per Image')
plt.title('Average Hay Bale Annotations per Hay Field')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------
# Figure 2: Boxplots for Each Hay Field
boxplot_data = []
labels = []
for sheet in sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    df = df.sort_values('image_id')
    boxplot_data.append(df['annotation_count'])
    labels.append(sheet)

plt.figure(figsize=(12, 8))
plt.boxplot(boxplot_data, labels=labels, patch_artist=True)
plt.xlabel('Hay Field')
plt.ylabel('Annotation Count')
plt.title('Distribution of Annotation Counts per Hay Field (Boxplot)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------
# Figure 3: Histograms for Each Hay Field (Subplots)
num_fields = len(sheet_names)
cols = 4
rows = (num_fields // cols) + (num_fields % cols > 0)

fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))
axes = axes.flatten()

for i, sheet in enumerate(sheet_names):
    df = pd.read_excel(xls, sheet_name=sheet)
    max_count = df['annotation_count'].max()
    # Use bins up to max_count + 2 to ensure we see the highest count clearly
    bins = range(0, max_count + 2)

    ax = axes[i]
    ax.hist(df['annotation_count'], bins=bins, color='lightgreen', edgecolor='black')
    ax.set_title(sheet, fontsize=16)

    # Only label the x-axis for subplots in the bottom row
    if i // cols == rows - 1:
        ax.set_xlabel('Annotation Count', fontsize=13)
        ax.tick_params(axis='x', labelrotation=45)

    # Only label the y-axis for subplots in the left column
    if i % cols == 0:
        ax.set_ylabel('Frequency', fontsize=13)

    ax.tick_params(axis='both', labelsize=10)

# Hide any unused subplots if the number of sheets < rows*cols
for j in range(len(sheet_names), len(axes)):
    axes[j].set_visible(False)

fig.suptitle("Histograms for Each Hay Field", fontsize=16)
plt.subplots_adjust(hspace=0.4, wspace=0.3)
plt.show()

# ---------------------------
# Figure 4: Subplots for Annotation Count vs Image ID for Each Hay Field (X-axis label only on last row)
num_fields = len(sheet_names)
cols = 4
rows = (num_fields // cols) + (num_fields % cols > 0)

# Enable constrained_layout for better spacing
fig, axes = plt.subplots(rows, cols, figsize=(20, 20), constrained_layout=True)
axes = axes.flatten()

for i, sheet in enumerate(sheet_names):
    df = pd.read_excel(xls, sheet_name=sheet)
    df = df.sort_values('image_id')
    ax = axes[i]
    ax.plot(df['image_id'], df['annotation_count'], marker='o', linestyle='-')

    # Subplot title
    ax.set_title(sheet, fontsize=16)

    # Always show the y-axis label
    ax.set_ylabel('Annotation Count', fontsize=13)
    ax.tick_params(axis='y', labelsize=8)

    # Only show the x-axis label if this subplot is in the bottom row
    if i // cols == rows - 1:
        ax.set_xlabel('Image ID', fontsize=13)
    # Otherwise, do not set the x-axis label (but keep the tick labels)

    # Rotate x-axis tick labels and use a slightly smaller font
    ax.tick_params(axis='x', labelrotation=45, labelsize=8)

# Hide any unused subplots if the number of sheets < rows * cols
for j in range(len(sheet_names), len(axes)):
    axes[j].set_visible(False)

# Main title for the figure
fig.suptitle("Annotation Count per Image for Each Hay Field", fontsize=16)
plt.show()

# ---------------------------
# Figure 5: Violin Plots for Each Hay Field
# Sort the sheet names naturally (i.e., Hay bales 1, 2, ... 16)
sorted_sheet_names = sorted(sheet_names, key=lambda x: int(x.split(" ")[-1]))
violin_data = []
for sheet in sorted_sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    violin_data.append(df['annotation_count'])

plt.figure(figsize=(12, 8))
plt.violinplot(violin_data, showmeans=True, showmedians=True)
plt.xticks(range(1, len(sorted_sheet_names) + 1), sorted_sheet_names, rotation=45)
plt.xlabel('Hay Field')
plt.ylabel('Annotation Count')
plt.title('Violin Plot of Annotation Counts per Hay Field')
plt.tight_layout()
plt.show()
