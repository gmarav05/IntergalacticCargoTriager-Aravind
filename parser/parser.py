import re
import json
import os

def parse_manifest(file_path):
    parsed_records = []
    
    # Pattern to match: [DATE] || CARGO_ID :: WEIGHT >> DESTINATION
    pattern = re.compile(r'^\[([\d-]+)\]\s*\|\|\s*([A-Z0-9-]+)\s*::\s*([\d.]+)\s*>>\s*(.+)$')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            
            match = pattern.match(line)
            if not match:
                print(f"Warning: Line {line_num} does not match expected format: {line}")
                continue
                
            date_str, cargo_id, weight_str, destination = match.groups()
            weight = float(weight_str)
            
            # Rule 1: Multiply by 1.45 if destination contains 'Sector-7'
            if 'Sector-7' in destination:
                weight = weight * 1.45
                
            # Round final weight to nearest whole number
            final_weight = int(weight + 0.5)
                
            parsed_records.append({
                "date": date_str,
                "cargo_id": cargo_id,
                "weight_in_kg": final_weight,
                "destination": destination
            })
            
    return parsed_records

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, 'manifest.txt')
    output_file = os.path.join(script_dir, 'output.json')
    
    records = parse_manifest(input_file)
    
    # Write to output.json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully processed manifest. {len(records)} records saved to {output_file}.")
    print(json.dumps(records, indent=2))

if __name__ == '__main__':
    main()
