import shutil
import os

def copy_file_to_folders(source_file, destination_folders, num_copies):
    # Kiểm tra và tạo bản sao của file cho mỗi thư mục và số lượng bản sao cần tạo
    for destination_folder in destination_folders:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for i in range(num_copies):
            file_name = f"{os.path.splitext(os.path.basename(source_file))[0]}_{i+1}{os.path.splitext(source_file)[1]}"
            destination_path = os.path.join(destination_folder, file_name)

            shutil.copy2(source_file, destination_path)

# Đường dẫn file nguồn (file cần sao chép)
source_file = r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\tk_diengiadung_brand_npage.ipynb"

# Danh sách đường dẫn thư mục đích (nơi bạn muốn sao chép file đến)
destination_folders = [r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\KAFF",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Kangaroo",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Karofi",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Kemei",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Kuvings",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Ladomax",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Nagakawa",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Panasonic",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Philips",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Rinnai",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Robot",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\SENKO",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Sharp",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\SMY",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Sunhouse",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Tefal",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Tiross",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Toshiba",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Xiaomi",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Bear",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\BLAUBERG",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Bluestone",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Bosch",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Comet",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\DeLonghi",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Electrolux",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Elmich",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\ERA",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\Eurosun",
    r"D:\CNTT\py_for_da\crawl_data_analyst\tiki\crawl_170124(12hdem) - Copy\diengiadung\brand\HAFELE"
    ]


# Số lượng bản sao muốn tạo
num_copies = 1

# Gọi hàm để sao chép file vào từng thư mục đích và tạo số lượng bản sao cần thiết
copy_file_to_folders(source_file, destination_folders, num_copies)
