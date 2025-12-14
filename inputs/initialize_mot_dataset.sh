#! /bin/bash
data_dir=$(dirname "$0")
zip_file="${data_dir}/video-data-mot.zip"


echo "Downloading MOT17 video dataset from Kaggle to ${zip_file}"
curl -L -o "${zip_file}" \
  https://www.kaggle.com/api/v1/datasets/download/daudshah/video-data-mot

# unzip the file
echo "unpacking the file to ${data_dir}"
unzip -o "${zip_file}" -d "${data_dir}"

echo "removing the zip file"
rm "${zip_file}"
