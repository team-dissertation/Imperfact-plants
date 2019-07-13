import numpy as np
#import bpy

#def draw_cube(verts):
 #   edges = [(0, 1), (0, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7), (0, 4), (1, 5), (2, 6), (3, 7)]
  #  mesh = bpy.data.meshes.new('Pyramid_Mesh')
   # mesh.from_pydata(verts, edges, [])
    #mesh.update()
    #pyramid = bpy.data.objects.new('Pyramid', mesh)
    #scene = bpy.context.scene
    #scene.objects.link(pyramid)
#def draw_line(point1,point2):
 #   line=[(0,1)]
  #  verts=[point1,point2]
   # mesh = bpy.data.meshes.new('Pyramid_Mesh')
    #mesh.from_pydata(verts, line, [])
    #mesh.update()
   # pyramid = bpy.data.objects.new('Pyramid', mesh)
   # scene = bpy.context.scene
   # scene.objects.link(pyramid)

def bresenham(point1,point2):
    x1=point1[0]
    y1=point1[1]
    z1=point1[2]
    x2=point2[0]
    y2=-point2[1]
    z2=point2[2]
    dx=abs(x2-x1);
    dy=abs(y2-y1);
    dz=abs(z2-z1);
    sx=np.sign(x2-x1)
    sy=np.sign(y2-y1)
    sz=np.sign(z2-z1)
    print("起点坐标：")
    print(x1,y1,z1)
    point_list=[(x1,y1,z1)] #start point
    point1=(x1,y1,z1)
    point2=(x2,y2,z2)# end point
    print("终点坐标:")
    print(point2)
    #draw_line(point1,point2)

    if dx>dy and dx>dz:
        x=x1
        y=y1
        z=z1
        d1=2*dy-dx
        d2=2*dz-dx
        for i in range(dx):
            x=x+sx
            if d1<0:

                y=y
                d1=d1+2*dy;
                if d2<0:
                    z=z
                    d2=d2+2*dz;
                else:
                    z=z+sz
                    d2=d2+2*(dz-dx)
            else:
                y=y+sy
                d1=d1+2*(dy-dx)
                if d2<0:
                    z=z
                    d2=d2+2*dz;
                else:
                    z=z+sz
                    d2=d2+2*(dz-dx)
            point_list.append((x,y,z))
    elif dy>dx and dy>dz:
         #print(dy)
        x = x1
        y = y1
        z = z1
        d1 = 2 * dx - dy
        d2 = 2 * dz - dy
        #print(x, y, z)
        for i in range(dy):
             y = y + sy
             if d1 < 0:
                 x = x
                 d1 = d1 + 2 * dx;
                 if d2 < 0:
                     z = z
                     d2 = d2 + 2 * dz;
                 else:
                     z = z + sz
                     d2 = d2 + 2 * (dz - dy)
             else:
                 x = x + sx
                 d1 = d1 + 2 * (dx - dy)
                 if d2 < 0:
                    z = z
                    d2 = d2 + 2 * dz;
                 else:
                    z = z + sz
                    d2 = d2 + 2 * (dz - dy)
             point_list.append((x, y, z))
    elif dz>dx and dz>dy:
        #print(dz)
        x = x1
        y = y1
        z = z1
        d1 = 2 * dx - dz
        d2 = 2 * dy - dz
        #print(x, y, z)
        for i in range(dz):
            z = z + sz
            if d1 < 0:
                x = x
                d1 = d1 + 2 * dx;
                if d2 < 0:
                    y =y
                    d2 = d2 + 2 * dy;
                else:
                    y = y + sy
                    d2 = d2 + 2 * (dy - dz)
            else:
                x = x + sx
                d1 = d1 + 2 * (dx - dz)
                if d2 < 0:
                    y =y
                    d2 = d2 + 2 * dy;
                else:
                    y = y + sy
                    d2 = d2 + 2 * (dy - dz)
            point_list.append((x, y, z))
    print("point_list:")
    print(point_list)
    #mesh = bpy.data.meshes.new('Pyramid_Mesh')
    #mesh.from_pydata(point_list, [], [])
    #mesh.update()
    #pyramid = bpy.data.objects.new('Pyramid', mesh)
    #scene = bpy.context.scene
    #scene.objects.link(pyramid)

# ##cube
    cube_list=[]
    for i in range(len(point_list)-1):
        n=np.array(point_list[i])
        m=np.array(point_list[i+1])
        a=m-n
        if abs(a[0]*a[1]*a[2]) ==1: # x,y,z different
            xmin=min(n[0],m[0])
            xmax=max(n[0],m[0])
            ymin=min(n[1],m[1])
            ymax=max(n[1],m[1])
            zmin=min(n[2],m[2])
            zmax=max(n[2],m[2])
            cube=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),(xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
            cube_list.append((xmin,ymin,zmin,xmax,ymax,zmax))
           # draw_cube(cube)


        #draw_cube(cube)

        #print(cube)
        elif a[0]==0 and abs(a[1])==1 and abs(a[2])==1: #same x value
            xmin = min(n[0],n[0]+sx)
            xmax = max(n[0], n[0] + sx)
            ymin = min(n[1], m[1])
            ymax = max(n[1], m[1])
            zmin = min(n[2], m[2])
            zmax = max(n[2], m[2])
            #print("value_x=0")
            if i ==0:
                cubex1 = [(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),(xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
                cube_list.append((xmin, ymin, zmin, xmax, ymax, zmax))
               # draw_cube(cubex1)
            else:
                cubex1=[(n[0],ymin,zmin),(n[0]+1,ymin,zmin),(n[0],ymax,zmin),(n[0]+1,ymax,zmin),(n[0],ymin,zmax),(n[0]+1,ymin,zmax),(n[0],ymax,zmax),(n[0]+1,ymax,zmax)]
                cubex2=[(n[0]-1,ymin,zmin),(n[0],ymin,zmin),(n[0]-1,ymax,zmin),(n[0],ymax,zmin),(n[0]-1,ymin,zmax),(n[0],ymin,zmax),(n[0]-1,ymax,zmax),(n[0],ymax,zmax)]
                cube_list.append((cubex1[0][0],cubex1[0][1],cubex1[0][2] ,cubex1[7][0],cubex1[7][1],cubex1[7][2]))
                cube_list.append((cubex2[0][0],cubex2[0][1],cubex2[0][2] ,cubex2[7][0],cubex1[7][1],cubex2[7][2]))
                #draw_cube(cubex1)
               # draw_cube(cubex2)

            #print(cubex1)
            #print(cubex2)
        elif a[1]==0 and abs(a[0])==1 and abs(a[2])==1: # same y value
            xmin=min(n[0],m[0])
            xmax=max(n[0],m[0])
            ymin=min(n[1],n[1]+sy)
            ymax = max(n[1], n[1] + sy)
            zmin=min(n[2],m[2])
            zmax=max(n[2],m[2])
            #print("value_y=0")
            if i ==0:
                cubey1 = [(xmin, ymin, zmin), (xmax, ymin, zmin), (xmin, ymax, zmin), (xmax,ymax, zmin),
                      (xmin, ymin, zmax), (xmax, ymin, zmax), (xmin, ymax, zmax), (xmax, ymax, zmax)]
                cube_list.append((xmin, ymin, zmin, xmax, ymax, zmax))
              #  draw_cube(cubey1)
            else:
                cubey1=[(xmin,n[1]-1,zmin),(xmax,n[1]-1,zmin),(xmin,n[1],zmin),(xmax,n[1],zmin),(xmin,n[1]-1,zmax),(xmax,n[1]-1,zmax),(xmin,n[1],zmax),(xmax,n[1],zmax)]
                cubey2=[(xmin,n[1],zmin),(xmax,n[1],zmin),(xmin,n[1]+1,zmin),(xmax,n[1]+1,zmin),(xmin,n[1],zmax),(xmax,n[1],zmax),(xmin,n[1]+1,zmax),(xmax,n[1]+1,zmax)]
                cube_list.append((cubey1[0][0],cubey1[0][1],cubey1[0][2] ,cubey1[7][0],cubey1[7][1],cubey1[7][2]))
                cube_list.append((cubey2[0][0], cubey2[0][1], cubey2[0][2], cubey2[7][0], cubey2[7][1], cubey2[7][2]))
              #  draw_cube(cubey1)
              #  draw_cube(cubey2)

            #print(cubey1)
            #print(cubey2)
        elif a[2]==0 and abs(a[1])==1 and abs(a[0])==1: #same z value
            xmin=min(n[0],m[0])
            xmax=max(n[0],m[0])
            ymin=min(n[1],m[1])
            ymax=max(n[1],m[1])
            zmin=min(n[2],n[2]+sz)
            zmax = max(n[2], n[2] + sz)
            #print("value_z=0")
            if i == 0:
                cubez1 = [(xmin, ymin, zmin), (xmax, ymin, zmin), (xmin, ymax, zmin), (xmax, ymax, zmin),
                      (xmin, ymin, zmax), (xmax, ymin, zmax), (xmin, ymax, zmax), (xmax, ymax, zmax)]
                cube_list.append((xmin, ymin, zmin, xmax, ymax, zmax))
               # draw_cube(cubez1)
            else:
                cubez1=[(xmin,ymin,n[2]-1),(xmax,ymin,n[2]-1),(xmin,ymax,n[2]-1),(xmax,ymax,n[2]-1),(xmin,ymin,n[2]),(xmax,ymin,n[2]),(xmin,ymax,n[2]),(xmax,ymax,n[2])]
                cubez2=[(xmin,ymin,n[2]),(xmax,ymin,n[2]),(xmin,ymax,n[2]),(xmax,ymax,n[2]),(xmin,ymin,n[2]+1),(xmax,ymin,n[2]+1),(xmin,ymax,n[2]+1),(xmax,ymax,n[2]+1)]
                cube_list.append((cubez1[0][0],cubez1[0][1],cubez1[0][2] ,cubez1[7][0],cubez1[7][1],cubez1[7][2]))
                cube_list.append((cubez2[0][0], cubez2[0][1], cubez2[0][2], cubez2[7][0], cubez2[7][1], cubez2[7][2]))
                #draw_cube(cubez1)
               # draw_cube(cubez2)
        elif a[0]==0 and a[1]==0 and a[2]!=0: # x1=x2.y1=y2
            if i ==0:
                z=np.array(point_list[i+2])# next next point
                xmin=min(abs(n[0]),abs(z[0]))*sx
                xmax=xmin+sx
                ymin=min(abs(n[1]),abs(z[1]))*sy
                ymax=ymin+sy
                zmin=min(n[2],m[2])
                zmax=max(n[2],m[2])
                cube2=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),
                    (xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
                cube_list.append((xmin, ymin, zmin, xmax, ymax, zmax))
              #  draw_cube(cube2)
            else:
                z=np.array(point_list[i-1])
                xmin=min(abs(n[0]),abs(z[0]))*sx
                xmax=xmin+sx
                ymin=min(abs(n[1]),abs(z[1]))*sy
                ymax=ymin+sy
                zmin=min(n[2],m[2])
                zmax=max(n[2],m[2])
                cube2=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),
                    (xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
                cube_list.append((xmin, ymin, zmin, xmax, ymax, zmax))
               # draw_cube(cube2)
        elif a[1]==0 and a[2]==0 and a[0]!=0: #y1=y2,z1=z2
            if i ==0:
                z=np.array(point_list[i+2])# next next point
                print("z=")
                print(z)
                xmin = min(n[0], m[0])
                xmax = max(n[0],m[0])
                ymin = min(abs(n[1]), abs(z[1])) * sy
                ymax = ymin + sy
                zmin = min(abs(n[2]), abs(z[2])) * sz
                zmax = zmin + sz
                cube2=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),
                    (xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
                cube_list.append((xmin, ymin, zmin, xmax, ymax, zmax))
                print(cube2)
                #draw_cube(cube2)
            else:
                z = np.array(point_list[i - 1])
                xmin = min(n[0], m[0])
                xmax = max(n[0],m[0])
                ymin = min(abs(n[1]), abs(z[1])) * sy
                ymax = ymin + sy
                zmin = min(abs(n[2]), abs(z[2])) * sz
                zmax = zmin + sz
                cube2=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),
                    (xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
                cube_list.append((xmin, ymin, zmin, xmax, ymax, zmax))
                print(cube2)
                #draw_cube(cube2)
    print("cube_list:")
    print(cube_list)
    return cube_list











