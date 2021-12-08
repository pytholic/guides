# Best way to uplaod dataset

## Link
[link](https://www.aboutdatablog.com/post/how-to-successfully-add-large-data-sets-to-google-drive-and-use-them-in-google-colab)

## Steps
* **Zip** the folder with the files
* Upload the zipped file using **Google Drive** Interface
* Open a new Google Colab file and `mount` it to Google Drive to be able to access the `zip` file
* Now extract files to the local environment with the following command.
  * !unzip gdrive/My\ Drive/data/train.zip
* Once you are comfortable that this command is working you can use the variation below that suppresses the output.
  * !unzip gdrive/My\ Drive/data/train.zip > /dev/null
* You can use the files for anything right now. Just access them from the new `train` folder
