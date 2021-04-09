# This file is used to parse the output data to organize it in a way to create the following
# average speed, min, max of a specific path.

# The format of the data is ["deltaX,deltaY,complete(1),....,deltaX_n,deltaY_n,complete(0)"]
from pathlib import Path
import math


def main():
    main_folder = Path("C:/Users/C0rbin/Documents/GitHub/BotDashboard/mouse_data__2020_12_04_lenny")
    main_folder_updated = Path(str(main_folder) + "_updated")
    if not main_folder_updated.exists():
        main_folder_updated.mkdir()

    files = main_folder.glob("*.json")

    for file in files:
        print(file)
        fh_out = open(main_folder_updated / file.name, "w")
        fh = open(file)
        updated_line = "[\n"
        for line in fh:
            if "[" in line or "]" in line:
                continue
            line = line.strip()
            # print(line)
            # Split the line so we can computer average velocity, high, and low movements

            # split_line = line.split(",")[2:]
            split_line = line.split(",")
            # skip first 2 since they are the "last delta". then it goes deltaX,deltaY
            # Time duration would be total/2 * 20ms
            # Finding distance would be as simple as deltaX^2 + deltaY^2 = distance^2 or Sqrt(deltaX^2 + deltaY^2)
            # angle would be Tan (deltaY/deltaX)
            total_duration_ms = len(split_line) / 3 * 20
            header = "x\t\ty\tcomplete\tdistance\tangle"

            # print("Total points ", len(split_line), "duration ms:", total_duration_ms)
            # print(header)
            updated_line += "\""

            ### TEMP CODE for lenny
            split_line[0] = split_line[0].replace("\"", "")
            front_data = split_line[0:4]  # ID, Random number, lastDeltaX, lastDeltaY
            updated_line += ",".join(front_data) + ","

            deltaX = float(front_data[2])
            deltaY = float(front_data[3])
            distance = math.sqrt(deltaX ** 2 + deltaY ** 2)
            if abs(deltaX) > 0:
                angle = math.degrees(math.atan(deltaY / deltaX))
            else:
                angle = 0

            updated_line += "{:1.4f}".format(distance) + "," + "{:3.4f}".format(angle) + ","
            ##### END TEMP CODE

            split_line = split_line[4:]  # Trimming off the front 4
            for i in range(0, len(split_line) - 1, 3):
                deltaX = float(split_line[i])
                deltaY = float(split_line[i + 1])
                complete = split_line[i + 2].replace("\"", "")
                distance = math.sqrt(deltaX ** 2 + deltaY ** 2)
                if abs(deltaX) > 0:
                    angle = math.degrees(math.atan(deltaY / deltaX))
                else:
                    angle = 0
                # print(deltaX, deltaY, complete, "{:1.4f}".format(distance), "{:3.4f}".format(angle), sep="\t")
                output = [str(deltaX), str(deltaY), str(complete), "{:1.4f}".format(distance), "{:3.4f}".format(angle)]
                updated_line += ",".join(output) + ","
            updated_line = updated_line[:-1]
            updated_line += "\",\n"
        updated_line = updated_line[:-2]
        updated_line += "\n]"
        fh_out.write(updated_line)
        fh_out.close()
        fh.close()


if __name__ == '__main__':
    main()

    # for i in range(-10,10):
    #     for j in range(-10,10):
    #         if j != 0:
    #             print(i, j, math.atan(i/j), math.degrees(math.atan(i/j)))
