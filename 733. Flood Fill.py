class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        defaultC = image[sr][sc]
        tempC = color
        color = "f"
        image[sr][sc] = color

        def change(image, defaultC, color):
            for j in range(0, len(image)):
                for k in range(0, len(image[0])):
                    if image[j][k] == color:
                        if k>0 and image[j][k-1] == defaultC: 
                            image[j][k-1] = color
    
                        if k+1<len(image[0]) and image[j][k+1] == defaultC :
                            image[j][k+1] = color

                        if j>0 and image[j-1][k]==defaultC:
                            image[j-1][k] = color
    
                        if j+1<len(image) and image[j+1][k] == defaultC:
                            image[j+1][k] = color
            return image

        for i in range(0, len(image)):
            image=change(image,defaultC,color)

        for i in range(0, len(image)):
            for j in range(0, len(image[i])):
                if image[i][j] == "f":
                    image[i][j] = tempC
                



        return image