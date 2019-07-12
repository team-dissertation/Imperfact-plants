import numpy as np
import bpy

def draw_cube(verts):
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7), (0, 4), (1, 5), (2, 6), (3, 7)]
    mesh = bpy.data.meshes.new('Pyramid_Mesh')
    mesh.from_pydata(verts, edges, [])
    mesh.update()
    pyramid = bpy.data.objects.new('Pyramid', mesh)
    scene = bpy.context.scene
    scene.objects.link(pyramid)
def draw_line(point1,point2):
    line=[(0,1)]
    verts=[point1,point2]
    mesh = bpy.data.meshes.new('Pyramid_Mesh')
    mesh.from_pydata(verts, line, [])
    mesh.update()
    pyramid = bpy.data.objects.new('Pyramid', mesh)
    scene = bpy.context.scene
    scene.objects.link(pyramid)

x1=0
y1=0
z1=0
x2=10
y2=-3
z2=-5
dx=abs(x2-x1);
dy=abs(y2-y1);
dz=abs(z2-z1);
sx=np.sign(x2-x1)
sy=np.sign(y2-y1)
sz=np.sign(z2-z1)
print(x1,y1,z1)
point=[(x1,y1,z1)] #start point
point1=(x1,y1,z1)
point2=(x2,y2,z2)# end point
draw_line(point1,point2)

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
        point.append((x,y,z))
elif dy>dx and dy>dz:
     #print(dy)
     x = x1
     y = y1
     z = z1
     d1 = 2 * dx - dy
     d2 = 2 * dz - dy
     print(x, y, z)
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
         point.append((x, y, z))
elif dz>dx and dz>dy:
     print(dz)
     x = x1
     y = y1
     z = z1
     d1 = 2 * dx - dz
     d2 = 2 * dy - dz
     print(x, y, z)
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
         point.append((x, y, z))
print(point)
mesh = bpy.data.meshes.new('Pyramid_Mesh')
mesh.from_pydata(point, [], [])
mesh.update()
pyramid = bpy.data.objects.new('Pyramid', mesh)
scene = bpy.context.scene
scene.objects.link(pyramid)

# ##cube

for i in range(len(point)-1):
    n=np.array(point[i])
    m=np.array(point[i+1])
    a=m-n
    if abs(a[0]*a[1]*a[2]) ==1: # x,y,z different
        xmin=min(n[0],m[0])
        xmax=max(n[0],m[0])
        ymin=min(n[1],m[1])
        ymax=max(n[1],m[1])
        zmin=min(n[2],m[2])
        zmax=max(n[2],m[2])
        cube=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),(xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
        draw_cube(cube)


        #draw_cube(cube)

        #print(cube)
    elif a[0]==0 and abs(a[1])==1 and abs(a[2])==1: #same x value
        ymin = min(n[1], m[1])
        ymax = max(n[1], m[1])
        zmin = min(n[2], m[2])
        zmax = max(n[2], m[2])
        #print("value_x=0")
        cubex1=[(n[0],ymin,zmin),(n[0]+1,ymin,zmin),(n[0],ymax,zmin),(n[0]+1,ymax,zmin),(n[0],ymin,zmax),(n[0]+1,ymin,zmax),(n[0],ymax,zmax),(n[0]+1,ymax,zmax)]
        cubex2=[(n[0]-1,ymin,zmin),(n[0],ymin,zmin),(n[0]-1,ymax,zmin),(n[0],ymax,zmin),(n[0]-1,ymin,zmax),(n[0],ymin,zmax),(n[0]-1,ymax,zmax),(n[0],ymax,zmax)]
        draw_cube(cubex1)
        draw_cube(cubex2)

        #print(cubex1)
        #print(cubex2)
    elif a[1]==0 and abs(a[0])==1 and abs(a[2])==1: # same y value
        xmin=min(n[0],m[0])
        xmax=max(n[0],m[0])
        zmin=min(n[2],m[2])
        zmax=max(n[2],m[2])
        #print("value_y=0")
        cubey1=[(xmin,n[1]-1,zmin),(xmax,n[1]-1,zmin),(xmin,n[1],zmin),(xmax,n[1],zmin),(xmin,n[1]-1,zmax),(xmax,n[1]-1,zmax),(xmin,n[1],zmax),(xmax,n[1],zmax)]
        cubey2=[(xmin,n[1],zmin),(xmax,n[1],zmin),(xmin,n[1]+1,zmin),(xmax,n[1]+1,zmin),(xmin,n[1],zmax),(xmax,n[1],zmax),(xmin,n[1]+1,zmax),(xmax,n[1]+1,zmax)]
        draw_cube(cubey1)
        draw_cube(cubey2)

        #print(cubey1)
        #print(cubey2)
    elif a[2]==0 and abs(a[1])==1 and abs(a[0])==1: #same z value
        xmin=min(n[0],m[0])
        xmax=max(n[0],m[0])
        ymin=min(n[1],m[1])
        ymax=max(n[1],m[1])
        #print("value_z=0")
        cubez1=[(xmin,ymin,n[2]-1),(xmax,ymin,n[2]-1),(xmin,ymax,n[2]-1),(xmax,ymax,n[2]-1),(xmin,ymin,n[2]),(xmax,ymin,n[2]),(xmin,ymax,n[2]),(xmax,ymax,n[2])]
        cubez2=[(xmin,ymin,n[2]),(xmax,ymin,n[2]),(xmin,ymax,n[2]),(xmax,ymax,n[2]),(xmin,ymin,n[2]+1),(xmax,ymin,n[2]+1),(xmin,ymax,n[2]+1),(xmax,ymax,n[2]+1)]
        draw_cube(cubez1)
        draw_cube(cubez2)
    elif a[0]==0 and a[1]==0 and a[2]!=0: # x1=x2.y1=y2
        if i ==0:
            z=np.array(point[i+2])# next next point
            xmin=min(abs(n[0]),abs(z[0]))*sx
            xmax=xmin+sx
            ymin=min(abs(n[1]),abs(z[1]))*sy
            ymax=ymin+sy
            zmin=min(n[2],m[2])
            zmax=max(n[2],m[2])
            cube2=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),
                    (xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
            draw_cube(cube2)
        else:
            z=np.array(point[i-1])
            xmin=min(abs(n[0]),abs(z[0]))*sx
            xmax=xmin+sx
            ymin=min(abs(n[1]),abs(z[1]))*sy
            ymax=ymin+sy
            zmin=min(n[2],m[2])
            zmax=max(n[2],m[2])
            cube2=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),
                    (xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
            draw_cube(cube2)
    elif a[1]==0 and a[2]==0 and a[0]!=0: #y1=y2,z1=z2
        if i ==0:
            z=np.array(point[i+2])# next next point
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
            print(cube2)
            draw_cube(cube2)
        else:
            z = np.array(point[i - 1])
            xmin = min(n[0], m[0])
            xmax = max(n[0],m[0])
            ymin = min(abs(n[1]), abs(z[1])) * sy
            ymax = ymin + sy
            zmin = min(abs(n[2]), abs(z[2])) * sz
            zmax = zmin + sz
            cube2=[(xmin,ymin,zmin),(xmax,ymin,zmin),(xmin,ymax,zmin),(xmax,ymax,zmin),
                    (xmin,ymin,zmax),(xmax,ymin,zmax),(xmin,ymax,zmax),(xmax,ymax,zmax)]
            print(cube2)
            draw_cube(cube2)









