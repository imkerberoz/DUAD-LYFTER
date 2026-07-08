#THIS CODE READS A LIST OF SONGS FROM A TEXT FILE, SORTS THEM ALPHABETICALLY,
#AND WRITES THE SORTED LIST TO A NEW TEXT FILE.
def sort_songs(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as input_f:
            songs = input_f.readlines()
        
        #REMOVE/STRIP WHITE SPACE AND EMPTY LINES
        songs = [song.strip() for song in songs if song.strip()]
        #SORT SONGS CASE-INSENSITIVELY (IGNORING CASE DIFFERENCES)
        songs.sort(key=lambda x: x.lower())
        
        #NOW WRITING THE SORTED SONGS TO A NEW FILE
        with open(output_file, 'w', encoding='utf-8') as output_f:
            for song in songs:
                output_f.write(song + '\n')
        
        print(f"Songs sorted successfully! Saved to '{output_file}'") #CONFIRMATION MESSAGE
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # DEFINE FULL PATHS FOR INPUT AND OUTPUT FILES
    input_filename  = r"C:\Users\dieeg\Downloads\PROGRAMACION\SEMANA 8\music.txt" #HERE WE DEFINE THE INPUT FILE PATH (CAN BE CHANGED AS NEEDED)
    output_filename = r"C:\Users\dieeg\Downloads\PROGRAMACION\SEMANA 8\SortedSongs.txt" #HERE WE DEFINE THE OUTPUT FILE PATH (CAN BE CHANGED AS NEEDED)
    
    sort_songs(input_filename, output_filename)