from PIL import Image 
  
# creating a image object 
im = Image.open("train.jpg")
WIDTH = im.size[0]
HEIGHT = im.size[1]
px = im.load() 

def get_vector_from_dir(v1, v2):
    return (v1[0] + v2[0]. v1[1] + v2[1])

def initialize_id_vector(width, height):
    return [[-1 for i in range(width)] for i in range(height)]

def color_diff(vec1, vec2):
    rdiff = abs(vec1[0] - vec2[0])
    gdiff = abs(vec1[1] - vec2[1])
    bdiff = abs(vec1[2] - vec2[2])
    return rdiff + gdiff + bdiff

def id_bodies_from_img(image, thrsh):
    WIDTH = image.size[0]
    HEIGHT = image.size[1]
    print(WIDTH)
    print(HEIGHT)
    px = image.load()
    bodies = initialize_id_vector(WIDTH, HEIGHT)

    for k in range(HEIGHT):
        for i in range(WIDTH):
            identify_pix(px, i, k, bodies, image.size, thrsh)
    

    # for k in range(HEIGHT):
    #     for i in range(WIDTH):
    #         print(bodies[i][k], end=" ")
    #     print()

    for k in range(WIDTH):
        for i in range(HEIGHT):
            px[k, i] = bodies[i][k], bodies[i][k], bodies[i][k] 

    im.show()
    return im

def identify_pix(px, i, k, bodies, size, thrsh):
    threshold = thrsh
    if (i == 0 and k == 0):
        bodies[k][i] = 0
        return
    if (i > 0):
        if (color_diff(px[i, k], px[i-1, k]) <= threshold):
            bodies[k][i] = bodies[k][i-1]
            return 
        if (k > 0):
            if (color_diff(px[i, k],  px[i-1, k-1]) <= threshold):
                bodies[k][i] = bodies[k-1][i-1]
                return
    if (k > 0):
        if (color_diff(px[i, k], px[i, k-1]) <= threshold):
            bodies[k][i] = bodies[k-1][i]
            return
        if (i < size[0]-1):
            if (color_diff(px[i, k], px[i+1, k-1]) <= threshold):
                bodies[k][i] = bodies[k-1][i+1]
                return
    
    bodies[k][i] = int((float(color_diff(px[i, k], (255,255,255)))/255)*(threshold+50))
         

# for i in range(WIDTH):
#     for k in range(HEIGHT):
#         print(px[i, k][0], end=" ")
#     print()


id_bodies_from_img(id_bodies_from_img(id_bodies_from_img(im, 40), 40), 40)

# print (px[4, 4]) 
# px[4, 4] = (0, 0) 
# print (px[4, 4]) 
# cordinate = x, y = 0, 0
  
# # using getpixel method 
# print (im.getpixel(cordinate));
