def scaledData(data):
    min_val = min(data)
    max_val = max(data)
    return [round((x - min_val) / (max_val - min_val) * 100, 2) for x in data]

# Test the function with sample data
sample_data = [1, 3, 4.5, 6.0, 7.5]

scaled_result = scaledData(sample_data)

print(f"Original Data: {sample_data}")
print(f"Scaled Data: {scaled_result}")
