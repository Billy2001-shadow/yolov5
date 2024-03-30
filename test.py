import yaml

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
            data = {}  # Return an empty dictionary in case of error
    return data

data = read_yaml_file('camera.yaml')

# Extract camera parameters
f_x = data['Camera']['IntrinsicParameters']['FocalLength'][0]
f_y = data['Camera']['IntrinsicParameters']['FocalLength'][1]
c_x = data['Camera']['IntrinsicParameters']['PrincipalPoint'][0]
c_y = data['Camera']['IntrinsicParameters']['PrincipalPoint'][1]
height = data['Camera']['Height']
fx, fy = data['Camera']['IntrinsicParameters']['FocalLength']
cx, cy = data['Camera']['IntrinsicParameters']['PrincipalPoint']
# k1, k2, p1, p2, k3 = data['Camera']['IntrinsicParameters']['DistortionCoefficients']
print(f_x, f_y, c_x, c_y,height)
print(fx, fy, cx, cy)