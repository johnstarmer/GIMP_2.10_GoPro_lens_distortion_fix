# GIMP_2.10_GoPro_lens_distortion_fix
A python script to remove distortion from underwater GoPro images in Gimp-2.10.
-----

# To load the script:
Download the [batch_lens_diistortion.py file](https://github.com/johnstarmer/GIMP_2.10_GoPro_lens_distortion_fix/blob/main/batch_lens_distortion.py).

On the top level dropdown menu in Gimp to Scripts > Python Fu > Console.

![PythonFuMenuLocation](https://github.com/johnstarmer/GIMP_2.10_GoPro_lens_distortion_fix/blob/main/ConsoleMenuLocation.png "Python Fu Console")

Once the console is open you'll want to run the following AFTER updating the file path to your script and saving it.  (e.g. A MacOS user might use ```execfile("/Users/jstarmer/Desktop/batch_lens_distortion.py")``` and a Windows user might use ```execfile("C:/Users/username/Desktop/batch_lens_distortion.py")```

Run:
```
execfile("/path/to/your/script/batch_lens_distortion.py")
```
Note: If you change the script parameters (e.g. degree of distortion), you must reload the script in the Python Fu console for changes to take effect.

# Example Usage:
``` python
input_folder = "/Users/jstarmer/Desktop/D_input"  
#Path to input folder with images
output_folder = "/Users/jstarmer/Desktop//D_output"  
#Path to output folder
```
To run the script, run the following in the Python Fu console:

```
batch_lens_distortion(input_folder, output_folder)
```

The script will save the altered files to the D_output folder (in this example) and leave the originals in the D_input folder.
