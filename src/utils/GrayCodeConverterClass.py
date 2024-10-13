from src.models.GAParametersClass import GAParameters


class GrayCodeConverter():
    
    @staticmethod
    def get_maximum_discharge(ga_parameters: GAParameters):
        maximum_discharge = []
        for set in ga_parameters.gene_sets:
            maximum_discharge.append(len(bin(len(set)-1)[2:]))
            
        return maximum_discharge
    
    @staticmethod
    def convert_to_code(value: [int], ga_parameters: GAParameters) -> str:
        gray_code = ""
        for i, v in enumerate(value):
            gray_number = v ^ (v >> 1)
            gray_binary = bin(gray_number)[2:]
            maximum_discharge = GrayCodeConverter.get_maximum_discharge(ga_parameters)
            gray_binary = gray_binary.zfill(maximum_discharge[i])
            gray_code = f'{gray_code}{gray_binary}'
        
        return gray_code
    
    @staticmethod
    def convert_from_code(code: str, ga_parameters: GAParameters) -> [int]:
        value = []
        j = 0
        maximum_discharge = GrayCodeConverter.get_maximum_discharge(ga_parameters)
        for md in maximum_discharge:
            part = code[j : j+md]
            binary = part[0]
            for i in range(1, len(part)):
                if part[i] == '1':
                   if binary[i-1] == '0':
                       binary += '1'
                   else:
                       binary += '0'
                else:
                    binary += binary[i-1] 
            value.append(int(binary, 2))
            j += md
                
        return value


if __name__ == "__main__":
    pass