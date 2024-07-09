from colorama import Fore, Style
SOLVED_STATE = {
    "F": [[1,2,3], [4,5,6], [7,8,9]],
    "R": [[10,11,12], [13,14,15], [16,17,18]],
    "B": [[19,20,21], [22,23,24], [25,26,27]],
    "L": [[28,29,30], [31,32,33], [34,35,36]],
    "U": [[37,38,39], [40,41,42], [43,44,45]],
    "D": [[46,47,48], [49,50,51], [52,53,54]]
}
class Cube:
    
    # ---------------------------------------------- Initialization and non-cube class functions and helper functions
    
    # Initializing the faces values
    def __init__(self) -> None:
        self.faces = SOLVED_STATE
    
    
    # print function overwrite
    def __str__(self):
        result = ""
        for face in ["F", "R", "B", "L", "U", "D"]:
            result += f"{face} Face:\n"
            for row in self.faces[face]:
                for num in row:
                    result += self.color_number(num) + " "
                result = result.strip() + "\n"
            result += "\n"
        return result.strip()

    # Helper function for above, assigns color to numbers according to their starting position, assumes white front, red top
    def color_number(self, num):
        if 1 <= num <= 9:
            return Fore.WHITE + str(num) + Style.RESET_ALL
        elif 10 <= num <= 18:
            return Fore.GREEN + str(num) + Style.RESET_ALL
        elif 19 <= num <= 27:
            return Fore.YELLOW + str(num) + Style.RESET_ALL
        elif 28 <= num <= 36:
            return Fore.BLUE + str(num) + Style.RESET_ALL
        elif 37 <= num <= 45:
            return Fore.RED + str(num) + Style.RESET_ALL
        elif 46 <= num <= 54:
            return Fore.MAGENTA + str(num) + Style.RESET_ALL
        return str(num)
    
    # function to repeat moves
    def rep(self, turn:str, rep:int):
        for _ in range(rep):
            match turn:
                case "x":
                    self.x()
                case "y":
                    self.y()
                case "z":
                    self.z()
                case "R":
                    self.R()
                case "L":
                    self.L()
                case "U":
                    self.U()
                case "D":
                    self.D()
                case "B":
                    self.B()
                case "F":
                    self.F()
                case "M":
                    self.M()
                case "E":
                    self.E()
                case "S":
                    self.S()
                case "r":
                    self.r()
                case "l":
                    self.l()
                case "f":
                    self.f()
                case "b":
                    self.b()
                case "u":
                    self.u()
                case "d":
                    self.d()
    
    # function to reverse a 3x3 matrix
    def reversal(self, matrix):
        # Flatten the matrix
        flattened = [item for sublist in matrix for item in sublist]

        # Reverse the flattened list
        reversed_flattened = flattened[::-1]

        # Reshape back into a 3x3 matrix
        reversed_matrix = [reversed_flattened[i:i+3] for i in range(0, len(reversed_flattened), 3)]

        return reversed_matrix

    # Function to execute an algorithm sequence
    def execute(self, seq:str):
        moves = seq.split(" ")
        for move in moves:
            if len(move) == 2:
               if move[1] == "'":
                   rep = 3
               else:
                   rep = 2
            else:
                rep = 1 
        
            self.rep(move[0], rep)
        
    # --------------------------------------- CUBE ROTATIONS -----------------------------------------------------------
    
    # X-ROTATIONS
    def x(self):
        faces = self.faces.copy()
        self.faces["U"] = faces["F"]
        self.faces["B"] = faces["U"]
        self.faces["D"] = faces["B"]
        self.faces["F"] = faces["D"]
        self.faces["R"] = self.rotate_r(faces["R"])
        self.faces["L"] = self.rotate_l(faces["L"])
    
    def x_prime(self):
        self.x()
        self.x()
        self.x()
        
    def x_2(self):
        self.x()
        self.x()
    
    
    # Y-ROTATIONS
    def y(self):
        faces = self.faces.copy()
        self.faces["F"] = self.reversal(faces["R"])
        self.faces["R"] = faces["B"]
        self.faces["B"] = self.reversal(faces["L"])
        self.faces["L"] = faces["F"]
        self.faces["U"] = self.rotate_r(faces["U"])
        self.faces["D"] = self.rotate_l(faces["D"])
    
    def y_prime(self):
        self.y()
        self.y()
        self.y()
    
    def y_2(self):
        self.y()
        self.y()
        
        
    # Z-ROTATIONS 
    def z(self):
        self.y_prime()
        self.x()
        self.y()
    
    def z_prime(self):
        self.z()
        self.z()
        self.z()
    
    def z_2(self):
        self.z()
        self.z()
        
        
        
    
    # ---------------------------------------------------------- FACE ROTATIONS --------------------------------------------------------------------
    
    # Rotate Right
    def rotate_r(self, face):
        return [list(row) for row in list(zip(*face[::-1]))]
    
    # Rotate Left 
    def rotate_l(self, face):
        return self.rotate_r(self.rotate_r(self.rotate_r(face)))
    
    
    # ---------------------------------------------------------- REPLACING FACES ---------------------------------------------------------------------
    
    # Replace Right
    def replace_R(self, start_values: list, end: str) -> None:
        for i in range(3):
            self.faces[end][i][2] = start_values[i]

    # Replace Left
    def replace_L(self, start_values: list, end: str) -> None:
        for i in range(3):
            self.faces[end][i][0] = start_values[i]

    # Replace Up
    def replace_U(self, origin: list, end: str): 
        self.faces[end][0] = origin
    
    # Replace Down
    def replace_D(self, origin: list, end: str): 
        self.faces[end][2] = origin
        
    # Replace Middle
    def replace_M(self, origin: list, end:list): 
        for i in range(3):
            end[i][1] = origin[i][1]

    # Replace Equator
    def replace_E(self, origin: list, end: list):
        end[1] = origin[1]
    
    
    # ---------------------------------------------------------------- SINGULAR FACE TURNS --------------------------------------------
    
    # Right Turn 
    def R(self):
        temp_F = [row[2] for row in self.faces["F"]]
        temp_U = [row[2] for row in self.faces["U"]]
        temp_B = [row[2] for row in self.faces["B"]]
        temp_D = [row[2] for row in self.faces["D"]]

        self.replace_R(temp_F, "U")
        self.replace_R(temp_U, "B")
        self.replace_R(temp_B, "D")
        self.replace_R(temp_D, "F")
        
        self.faces["R"] = self.rotate_r(self.faces.copy()["R"])
        
    # Left Turn
    def L(self):
        self.z_2()
        self.R()
        self.z_2()
    # Up Turn
    def U(self):
        self.z()
        self.R()
        self.z_prime()
    
    # Down Turn
    def D(self):
        self.z_prime()
        self.R()
        self.z()
    
    # Front Turn
    def F(self):
        self.y_prime()
        self.R()
        self.y()


    # Back Turn
    def B(self):
        self.y()
        self.R()
        self.y_prime()
    
    # ------------------------------------------------------- SLICE TURNS --------------------------------------------------- 
    # Middle turn
    def M(self):
        self.R()
        self.rep("L", 3)
        self.x_prime()
    
    # Equatorial Turn
    def E(self):
        self.U()
        self.rep("D", 3)
        self.y_prime()

    # Slice Turn
    def S(self):
        self.rep("F", 3)
        self.B()
        self.z()
    
    # ---------------------------------------------------------- WIDE TURNS ---------------------------------------------------------
    # Right wide turn
    def r(self):
        self.R()
        self.rep("M", 3)
    
    # Left wide turn
    def l(self):
        self.L()
        self.M()
        
    # Front wide turn
    def f(self):
        self.F()
        self.S()
    
    # Back wide turn
    def b(self):
        self.B()
        self.rep("S", 3)
    
    # Up wide turn
    def u(self):
        self.U()
        self.rep("E", 3)
    
    # Down wide turn
    def d(self):
        self.D()
        self.E()



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






      
 
    
    
        