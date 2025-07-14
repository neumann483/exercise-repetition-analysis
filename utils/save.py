# Save points to a CSV file
import csv


def save_keypoints_to_csv(keypoints_data: list, csv_path: str):
    if not keypoints_data:
        raise ValueError("No keypoints data to save.")

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Auto-generate header from first time
        header = ['frame_index']
        num_keypoints = len(keypoints_data[0]['keypoints'])

        for i in range(num_keypoints):
            header += [f'kp{i}_x', f'kp{i}_y', f'kp{i}_z', f'kp{i}_conf']
        writer.writerow(header)

        # Write data rows
        for frame_data in keypoints_data:
            row = [frame_data['frame_index']]
            for kp in frame_data['keypoints']:
                row += [
                    round(kp.get('x', 0), 5),
                    round(kp.get('y', 0), 5),
                    round(kp.get('z', 0), 5),
                    round(kp.get('confidence', 1.0), 3)
                ]
            writer.writerow(row)
        print(f'File successfully saved to {csv_path}')

