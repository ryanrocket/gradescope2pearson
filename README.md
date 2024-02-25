# gradescope2pearson
Sick and tired of entering grade manually. This will take the exported grades for an assignment in gradescope and allow it to be uploaded to the Pearon MyLab grade book.

### Usage
1. Export grades from Gradescope as a CSV file.
2. If you have students in Gradescope who use a name that is different than in Pearson's, you can create a JSON file with the following format:
```json
{
    "Gradescope First Name#Last Name": "Pearson First Name#Last Name",
    "Ryan#Wans", "Ryan M#Wans"
}
```
   Note the usage of a `#` to separate the first and last name. This is to avoid any issues with commas in the names. Passing this file is optional. If there any differences between names, Pearson will alert you when uploading the file. You can make changes accordingly in this JSON file. 
   
3. Run the script with the following command:
```bash
python3 transfer.py <gradescope.csv> <pearson.csv> <preferred_names.json>(OPTIONAL)
```
4. Ensure the paths of the files are correct.
5. Always check the output file to ensure the grades are correct.

If all runs well, you should see something like the following:
```bash
Running with preferred names being replaced...
Input file: /Users/rwans/Downloads/HW2_scores.csv
Output file: /Users/rwans/Downloads/HW2_pearson.csv
Starting transfer process...
File created successfully at /Users/rwans/Downloads/HW2_pearson.csv
Importing grades of 43 students.
Student's preferred name replaced: **************
Student's preferred name replaced: **************
Student's preferred name replaced: **************
Student's preferred name replaced: **************
Student's preferred name replaced: **************
Student's preferred name replaced: **************
Student's preferred name replaced: **************
Transfered grades of 43 students.
```
Or, if you don't have a preferred names file:
```bash
Input file: /Users/rwans/Downloads/HW2_scores.csv
Output file: /Users/rwans/Downloads/HW2_pearson.csv
Starting transfer process...
File created successfully at /Users/rwans/Downloads/HW2_pearson.csv
Importing grades of 43 students.
Transfered grades of 43 students.
```

### Batch Mode
If you have multiple assignments to transfer, you can use the batch mode. This will allow you to transfer multiple assignments without having to run the script multiple times.
1. Create a JSON file that details the batch in the following format:
```json
{
    "PathToGradescopeCSV1": "PathToPearsonCSV1",
    "PathToGradescopeCSV2": "PathToPearsonCSV2",
}
```
2. Run the script with the following command:
```bash
python3 batch.py <batch.json> <preferred_names.json>(OPTIONAL)
```