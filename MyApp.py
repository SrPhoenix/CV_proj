from math import pi, sin, cos


from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *
from direct.showbase.ShowBaseGlobal import globalClock
from direct.actor.Actor import Actor
import gltf
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import AntialiasAttrib
from panda3d.core import Point3
import math
from panda3d.core import PointLight

class MyApp(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)
        
        #window
        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)
        getModelPath().appendDirectory('/home/borges/CV_proj/models/car1')
        getModelPath().appendDirectory('/home/borges/CV_proj/models/car2')
        getModelPath().appendDirectory('/home/borges/CV_proj/models/ground')

        # self.loader.getMoadelPath().appendDirectory("/home/borges/CV_proj/models/car1")
        # self.loader.getMoadelPath().appendDirectory("/home/borges/CV_proj/models/car2")



        self.shader = Shader.load(Shader.SL_GLSL,
                            vertex="myshader.vert",
                            fragment="myshader.frag")

        self.phong = Shader.load(Shader.SL_GLSL,
                            vertex="phong.vert",
                            fragment="phong.frag")


        self.dayColors = [Vec4(0.8, 0.9, 1, 1), # midday
             Vec4(0.0549, 0.0980, 0.2588, 1)] # nighttime

        self.backgroundColor =Vec4(0.8, 0.9, 1, 1)
        self.lightPosition = Vec3(0,-1,-0.5)
        self.lightColor = Vec4(1,1,1,1)
        self.set_background_color(self.backgroundColor)

        self.timeOfDay = 0
        self.handLightPosition= Vec3(0,-20,2)

        alight = AmbientLight('alight')
        alight.setColor((0.2, 0.2, 0.2, 1))
        alnp = self.render.attachNewNode(alight)
        self.render.setLight(alnp)

        self.directionalLight = DirectionalLight("directionalLight")
        self.directionalLight.setDirection(Vec3(0, 0, -1))
        self.directionalLight.setColor(Vec4(1, 1, 1, 1))
        self.directionalLightNodePath = self.render.attachNewNode(self.directionalLight)
        self.render.setLight(self.directionalLightNodePath)



        house_light_1 = PointLight("House light 1")
        house_light_1.setColor((1,1,1,1))
        self.house_light_1_NodePath = self.render.attachNewNode(house_light_1)
        self.house_light_1_NodePath.setPos(-10,-10,10)
        self.render.setLight(self.house_light_1_NodePath)





        house_light_2 = PointLight("House light 2")
        house_light_2.setColor((1,1,1,1))
        self.house_light_2_NodePath = self.render.attachNewNode(house_light_2)
        self.house_light_2_NodePath.setHpr(-45, 45, 0)
        self.house_light_2_NodePath.setPos(6,5,1)
        self.render.setLight(self.house_light_2_NodePath)


        house_light_3 = PointLight("House light 3")
        house_light_3.setColor((1,1,1,1))
        self.house_light_3_NodePath = self.render.attachNewNode(house_light_3)
        self.house_light_3_NodePath.setHpr(-45, 45, 0)
        self.house_light_3_NodePath.setPos(6,-5,1)
        self.render.setLight(self.house_light_3_NodePath)

        lamp_light = PointLight("Lamp Light 1")
        lamp_light.setColor((1,1,1,1))
        self.lamp_light_NodePath = self.render.attachNewNode(lamp_light)
        self.lamp_light_NodePath.setPos(-10,-10,10)
        self.render.setLight(self.lamp_light_NodePath)



        moon = PointLight("moon")
        moon.setColor((1,1,1,1))
        self.moon_NodePath = self.render.attachNewNode(moon)
        self.moon_NodePath.setHpr(-45, 45, 0)
        self.moon_NodePath.setPos(10000,10000,10000)




        lamp_light_1 = PointLight("Lamp Light 1")
        lamp_light_1.setColor((1,1,1,1))
        self.lamp_light_1_NodePath = self.render.attachNewNode(lamp_light_1)
        self.lamp_light_1_NodePath.setHpr(-45, 45, 0)
        self.lamp_light_1_NodePath.setPos(-3.5,-15,3)
        self.render.setLight(self.lamp_light_1_NodePath)

        lamp_light_2 = PointLight("Lamp Light 2")
        lamp_light_2.setColor((1,1,1,1))
        self.lamp_light_2_NodePath = self.render.attachNewNode(lamp_light_2)
        self.lamp_light_2_NodePath.setHpr(-45, 45, 0)
        self.lamp_light_2_NodePath.setPos(3.5,-15,3)
        self.render.setLight(self.lamp_light_2_NodePath)





        # Load the ground model.
        self.scene = self.loader.loadModel("models/ground/scene.gltf")
        # Reparent the model to render.

        self.scene.setScale(30, 30, 20)
        self.scene.setPos(0,0,-5.3)

        # self.scene.setTexture(self.colorTex,1)

        self.normalMap = self.loader.loadTexture("/home/borges/CV_proj/textures/Cobblestone_normal.png")
        ts = TextureStage('ts')
        ts.setMode(TextureStage.MNormal)
        self.scene.setTexture(ts,self.normalMap)
        self.scene.reparentTo(self.render)



        #apply scenery, like buildings and lamps

        self.build1 = self.loader.loadModel("models/builds/BuildingCluster1/BuildingCluster1.egg")
        self.build1.setScale(0.5,0.5,0.5)
        self.build1.setPos(40,100,-2.3)
        self.build1.reparentTo(self.render)
        

        self.build2 = self.loader.loadModel("models/builds/BuildingCluster2/BuildingCluster2.egg")
        self.build2.setScale(0.5,0.5,0.5)
        self.build2.setPos(20,100,-2.3)
        self.build2.reparentTo(self.render)


        self.build3 = self.loader.loadModel("models/builds/BuildingCluster3/BuildingCluster3.egg")
        self.build3.setScale(0.5,0.5,0.5)
        self.build3.setPos(0,100,-2.3)
        self.build3.reparentTo(self.render)

        self.build4 = self.loader.loadModel("models/builds/BuildingCluster4/BuildingCluster4.egg")
        self.build4.setScale(0.5,0.5,0.5)
        self.build4.setPos(-20,100,-2.3)
        self.build4.reparentTo(self.render)

        self.build5 = self.loader.loadModel("models/builds/BuildingCluster5/BuildingCluster5.egg")
        self.build5.setScale(0.5,0.5,0.5)
        self.build5.setPos(-40,100,-2.3)
        self.build5.reparentTo(self.render)


        #Another row (back)
        self.build1 = self.loader.loadModel("models/builds/BuildingCluster1/BuildingCluster1.egg")
        self.build1.setScale(0.5,0.5,0.5)
        self.build1.setPos(40,-100,-2.3)
        self.build1.reparentTo(self.render)
        

        self.build2 = self.loader.loadModel("models/builds/BuildingCluster2/BuildingCluster2.egg")
        self.build2.setScale(0.5,0.5,0.5)
        self.build2.setPos(20,-100,-2.3)
        self.build2.reparentTo(self.render)


        self.build3 = self.loader.loadModel("models/builds/BuildingCluster3/BuildingCluster3.egg")
        self.build3.setScale(0.5,0.5,0.5)
        self.build3.setPos(0,-100,-2.3)
        self.build3.reparentTo(self.render)

        self.build4 = self.loader.loadModel("models/builds/BuildingCluster4/BuildingCluster4.egg")
        self.build4.setScale(0.5,0.5,0.5)
        self.build4.setPos(-20,-100,-2.3)
        self.build4.reparentTo(self.render)

        self.build5 = self.loader.loadModel("models/builds/BuildingCluster5/BuildingCluster5.egg")
        self.build5.setScale(0.5,0.5,0.5)
        self.build5.setPos(-40,-100,-2.3)
        self.build5.reparentTo(self.render)


        #Another row (right)
        self.build1 = self.loader.loadModel("models/builds/BuildingCluster1/BuildingCluster1.egg")
        self.build1.setScale(0.5,0.5,0.5)
        self.build1.setPos(70,80,-2.3)
        self.build1.reparentTo(self.render)
        

        self.build2 = self.loader.loadModel("models/builds/BuildingCluster2/BuildingCluster2.egg")
        self.build2.setScale(0.5,0.5,0.5)
        self.build2.setPos(70,60,-2.3)
        self.build2.reparentTo(self.render)


        self.build3 = self.loader.loadModel("models/builds/BuildingCluster3/BuildingCluster3.egg")
        self.build3.setScale(0.5,0.5,0.5)
        self.build3.setPos(70,40,-2.3)
        self.build3.reparentTo(self.render)

        self.build4 = self.loader.loadModel("models/builds/BuildingCluster4/BuildingCluster4.egg")
        self.build4.setScale(0.5,0.5,0.5)
        self.build4.setPos(70,20,-2.3)
        self.build4.reparentTo(self.render)

        self.build5 = self.loader.loadModel("models/builds/BuildingCluster5/BuildingCluster5.egg")
        self.build5.setScale(0.5,0.5,0.5)
        self.build5.setPos(70,0,-2.3)
        self.build5.reparentTo(self.render)


        self.build1 = self.loader.loadModel("models/builds/BuildingCluster1/BuildingCluster1.egg")
        self.build1.setScale(0.5,0.5,0.5)
        self.build1.setPos(70,-80,-2.3)
        self.build1.reparentTo(self.render)
        

        self.build2 = self.loader.loadModel("models/builds/BuildingCluster2/BuildingCluster2.egg")
        self.build2.setScale(0.5,0.5,0.5)
        self.build2.setPos(70,-40,-2.3)
        self.build2.reparentTo(self.render)


        self.build3 = self.loader.loadModel("models/builds/BuildingCluster3/BuildingCluster3.egg")
        self.build3.setScale(0.5,0.5,0.5)
        self.build3.setPos(70,-60,-2.3)
        self.build3.reparentTo(self.render)

        self.build4 = self.loader.loadModel("models/builds/BuildingCluster4/BuildingCluster4.egg")
        self.build4.setScale(0.5,0.5,0.5)
        self.build4.setPos(70,-100,-2.3)
        self.build4.reparentTo(self.render)

        self.build5 = self.loader.loadModel("models/builds/BuildingCluster5/BuildingCluster5.egg")
        self.build5.setScale(0.5,0.5,0.5)
        self.build5.setPos(70,-20,-2.3)
        self.build5.reparentTo(self.render)


        #Last Row!! (Left)
        self.build1 = self.loader.loadModel("models/builds/BuildingCluster1/BuildingCluster1.egg")
        self.build1.setScale(0.5,0.5,0.5)
        self.build1.setPos(-70,80,-2.3)
        self.build1.reparentTo(self.render)
        

        self.build2 = self.loader.loadModel("models/builds/BuildingCluster2/BuildingCluster2.egg")
        self.build2.setScale(0.5,0.5,0.5)
        self.build2.setPos(-70,60,-2.3)
        self.build2.reparentTo(self.render)


        self.build3 = self.loader.loadModel("models/builds/BuildingCluster3/BuildingCluster3.egg")
        self.build3.setScale(0.5,0.5,0.5)
        self.build3.setPos(-70,40,-2.3)
        self.build3.reparentTo(self.render)

        self.build4 = self.loader.loadModel("models/builds/BuildingCluster4/BuildingCluster4.egg")
        self.build4.setScale(0.5,0.5,0.5)
        self.build4.setPos(-70,20,-2.3)
        self.build4.reparentTo(self.render)

        self.build5 = self.loader.loadModel("models/builds/BuildingCluster5/BuildingCluster5.egg")
        self.build5.setScale(0.5,0.5,0.5)
        self.build5.setPos(-70,0,-2.3)
        self.build5.reparentTo(self.render)


        self.build1 = self.loader.loadModel("models/builds/BuildingCluster1/BuildingCluster1.egg")
        self.build1.setScale(0.5,0.5,0.5)
        self.build1.setPos(-70,-80,-2.3)
        self.build1.reparentTo(self.render)
        

        self.build2 = self.loader.loadModel("models/builds/BuildingCluster2/BuildingCluster2.egg")
        self.build2.setScale(0.5,0.5,0.5)
        self.build2.setPos(-70,-40,-2.3)
        self.build2.reparentTo(self.render)


        self.build3 = self.loader.loadModel("models/builds/BuildingCluster3/BuildingCluster3.egg")
        self.build3.setScale(0.5,0.5,0.5)
        self.build3.setPos(-70,-60,-2.3)
        self.build3.reparentTo(self.render)

        self.build4 = self.loader.loadModel("models/builds/BuildingCluster4/BuildingCluster4.egg")
        self.build4.setScale(0.5,0.5,0.5)
        self.build4.setPos(-70,-100,-2.3)
        self.build4.reparentTo(self.render)

        self.build5 = self.loader.loadModel("models/builds/BuildingCluster5/BuildingCluster5.egg")
        self.build5.setScale(0.5,0.5,0.5)
        self.build5.setPos(-70,-20,-2.3)
        self.build5.reparentTo(self.render)

        # Sound
        self.mySound = self.loader.loadSfx("CitySounds.mp3")
        self.mySound.setVolume(0.5)
        self.mySound.play()


        #SKYCUBE WITH TEXTURES
        # self.cube = self.loader.loadCubeMap('cube_#.png')

        # self.spaceSkyBox = self.loader.loadModel('models/Cube.egg')
        # self.spaceSkyBox.setScale(1000)
        # self.spaceSkyBox.setBin('background', 0)
        # self.spaceSkyBox.setDepthWrite(0)
        # self.spaceSkyBox.setTwoSided(True)
        # self.spaceSkyBox.setTexture(self.cube, 1)
        # self.spaceSkyBox.reparentTo(self.render)




        # self.ball = self.loader.loadModel("models/Sphere_HighPoly.egg")
        # self.ball.setPos(-7, 0, 1)
        # self.ball.setScale(0.25)
        # self.ball.reparentTo(self.render)
        # self.tex = self.loader.loadCubeMap('enviromnent_cube_#.jpg')
        # self.ball.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeCubeMap)
        # self.ball.setTexture(self.tex)



        view_matrix = self.cam.get_mat()
        self.viewPos = render.get_relative_point(render, view_matrix.get_row3(3))
        self.house = self.loader.loadModel("models/house/new_house.obj")

        # Apply scale and position transforms on the model.
        self.house.setScale(0.5, 0.5, 0.5)


        self.house.setPos(0, 0, 2.1)
        self.house.setHpr(self.house, 90)
        self.house.reparentTo(self.render)

        lightColor = Vec4(0.8, 0.9, 1, 1) # the position of the light source
        ambient = (0.2, 0.2, 0.2, 1.0) # the ambient color of the light
        diffuse = (0.5, 0.5, 0.5, 1.0) # the diffuse color of the light
        specular = (0.7, 0.7, 0.7, 1.0) # the specular color of the light
        viewPos = (0, 0, 5, 1) # the position of the viewer

        self.house.setShaderInput("lightColor", lightColor)
        self.house.setShaderInput("ambient", ambient)
        self.house.setShaderInput("diffuse", diffuse)
        self.house.setShaderInput("specular", specular)
        self.house.setShaderInput("viewPos", viewPos)


        phong_shader = Shader.load(Shader.SL_GLSL, "testing.vert", "testing.frag")

        #self.house.setShader(phong_shader)
        


        self.car_x = 7
        self.car_y = 0
        self.car_z = 0.55
        self.car = self.loader.loadModel('models/StationWagon/StationWagon.egg')
        self.car.setPos(self.car_x, self.car_y, self.car_z)
        self.car.setScale(0.25)

        self.car.reparentTo(self.render)

        self.lamp1 = self.loader.loadModel('models/LampPost/LampPost.egg')
        self.lamp1.setPos(-4,-15,0)
        self.lamp1.setHpr(self.lamp1, -90,0,0)
        self.lamp1.setScale(0.25)

        self.lamp1.reparentTo(self.render)


        self.lamp2 = self.loader.loadModel('models/LampPost/LampPost.egg')
        self.lamp2.setPos(4,-15,0)
        self.lamp2.setHpr(self.lamp2, 90,0,0)
        self.lamp2.setScale(0.25)

        self.lamp2.reparentTo(self.render)
        

        #code for first person view
        self.disableMouse()

        self.cameraModel = self.loader.loadModel("models/camera")
        self.cameraModel.reparentTo(self.render)
        self.cameraModel.setPos(0, -20, 2)

        self.camera.reparentTo(self.cameraModel)


        self.keyMap = {"w" : False, "s" : False, "a" : False, "d" : False, "space": False, "shift": False, "c": False, "l": False, "h": False, "p": False, "0": False, "1":False, "2":False}

        self.accept("w", self.setKey, ["w", True])
        self.accept("s", self.setKey, ["s", True])
        self.accept("a", self.setKey, ["a", True])
        self.accept("d", self.setKey, ["d", True])
        self.accept("0", self.lightControl, ["0"])
        self.accept("1", self.lightControl, ["1"])
        self.accept("2", self.lightControl, ["2"])
        self.accept("c", self.lightControl, ["c"])
        self.accept("l", self.lightControl, ["l"])
        self.accept("h", self.lightControl, ["h"])
        self.accept("p", self.lightControl, ["p"])

        self.accept("s-up", self.setKey, ["s", False])
        self.accept("a-up", self.setKey, ["a", False])
        self.accept("d-up", self.setKey, ["d", False])
        self.accept("w-up", self.setKey, ["w", False])

        self.accept("space", self.setKey, ["space", True])
        self.accept("space-up", self.setKey, ["space", False])

        self.accept("shift", self.setKey, ["shift", True])
        self.accept("shift-up", self.setKey, ["shift", False])



        self.taskMgr.add(self.cameraControl, "Camera Control")
        self.taskMgr.add(self.updateLights, "Update Lights")
        self.render.setAntialias(AntialiasAttrib.MAuto)
        carLight_r= PointLight("car light right")
        self.carLight_r_Np = self.render.attachNewNode(carLight_r)
        self.carLight_r_Np.setPos(7.0,17.0, 1)
        self.carLight_r_Np.reparentTo(self.car)
        self.render.setLight(self.carLight_r_Np)

        carLight_l= PointLight("car light Left")
        self.carLight_l_Np = self.render.attachNewNode(carLight_l)
        self.carLight_l_Np.setPos(8.0,17.0, 1)
        self.carLight_l_Np.reparentTo(self.car)
        self.render.setLight(self.carLight_l_Np)






        # Sphere 1, sphere with mirror like texture
        # Create a sphere with radius 0.4
        self.sphere = self.loader.loadModel("models/Sphere.egg")
        self.sphere.setScale(0.4)
        self.sphere.reparentTo(self.render)
        # Set the sphere's position and orientation
        self.sphere.setPos(10, 0, 1.5)
        self.sphere.setHpr(0, 0, 0)

        self.saveSphereMap('sphereReflect.jpg')
        self.tex = self.loader.loadTexture('sphereReflect.jpg')
        #self.sphere.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeSphereMap)
        self.sphere.setTexture(self.tex)

        #self.sphere.setShader(self.phong)



        # Sphere 2, sphere with metal like texture properties, which shines more than other spheres
        self.sphere2 = self.loader.loadModel("models/Sphere.egg")
        self.sphere2.setScale(0.4)
        self.sphere2.reparentTo(self.render)
        # Set the spheres positions and orientations
        self.sphere2.setPos(10, 5, 1.5)
        sphereMaterial= Material()
        sphereMaterial.setShininess(100)
        sphereMaterial.setSpecular((1,1,1,1))
        self.sphere2.setMaterial(sphereMaterial)


        # Sphere 3, sphere with earth texture and a normal map applied to it
        self.sphere3 = self.loader.loadModel("models/Sphere.egg")
        self.sphere3.setScale(0.4)
        self.sphere3.reparentTo(self.render)
        self.sphere3.setPos(10, -5, 1.5)

        self.worldTex= self.loader.loadTexture("textures/2k_earth_daymap.jpg")
        self.sphere3.setTexture(self.worldTex, 1)

        self.normalWorld = self.loader.loadTexture("textures/earth-normalmap.jpg")
        textureStage = TextureStage('ts')
        textureStage.setMode(TextureStage.MNormal)
        self.sphere3.setTexture(ts,self.normalWorld)

        # Sphere 4, sphere with height map of iceland applied
        self.sphere4 = self.loader.loadModel("models/Sphere.egg")
        self.sphere4.setScale(0.4)
        self.sphere4.reparentTo(self.render)
        self.sphere4.setPos(10, 10, 1.5)

        self.heightMap = self.loader.loadTexture("textures/heightmap.png")
        textureStage = TextureStage('ts')
        textureStage.setMode(TextureStage.MHeight)
        self.sphere3.setTexture(ts,self.heightMap)

        # Sphere 5, sphere with goraud shader applied
        self.sphere5 = self.loader.loadModel("models/Sphere.egg")
        self.sphere5.setScale(0.4)
        self.sphere5.reparentTo(self.render)
        self.sphere5.setPos(10, -10, 1.5)


        # Set more cars
        self.car1 = self.loader.loadModel('models/car2/scene.gltf')
        self.car1.setPos(-20,100,0.55)
        self.car1.setScale(0.2)
        self.car1.setHpr(self.car1, -180, 0,0)

        self.car1.reparentTo(self.render)

        self.car1.posInterval(20, Point3(-20,100,0.55), Point3(-20,-100,0.55)).loop()


        self.car2 = self.loader.loadModel('models/car2/scene.gltf')
        self.car2.setPos(-20,80,0.55)
        self.car2.setScale(0.2)
        self.car2.setHpr(self.car2, -180, 0,0)

        self.car2.reparentTo(self.render)

        self.sq1= Sequence(self.car2.posInterval(20, Point3(-20,80,0.55), Point3(-20,-100,0.55)), self.car2.posInterval(20, Point3(-20,100,0.55), Point3(-20,80,0.55)))
        self.sq1.loop()



        self.car3 = self.loader.loadModel('models/car2/scene.gltf')
        self.car3.setPos(-20,30,0.55)
        self.car3.setScale(0.2)
        self.car3.setHpr(self.car3, -180, 0,0)

        self.car3.reparentTo(self.render)

        self.sq2= Sequence(self.car3.posInterval(20, Point3(-20,30,0.55), Point3(-20,-100,0.55)), self.car3.posInterval(20, Point3(-20,100,0.55), Point3(-20,30,0.55)))
        self.sq2.loop()



        self.car4 = self.loader.loadModel('models/car2/scene.gltf')
        self.car4.setPos(-20,-10,0.55)
        self.car4.setScale(0.2)
        self.car4.setHpr(self.car4, -180, 0,0)

        self.car4.reparentTo(self.render)

        self.sq3= Sequence(self.car4.posInterval(20, Point3(-20,-10,0.55), Point3(-20,-100,0.55)), self.car4.posInterval(20, Point3(-20,100,0.55), Point3(-20,-10,0.55)))
        self.sq3.loop()


        self.car5 = self.loader.loadModel('models/car2/scene.gltf')
        self.car5.setPos(-24,-100,0.55)
        self.car5.setScale(0.2)

        self.car5.reparentTo(self.render)

        self.car5.posInterval(20, Point3(-24,-100,0.55), Point3(-24,100,0.55)).loop()


        self.car6 = self.loader.loadModel('models/car2/scene.gltf')
        self.car6.setPos(-24,-70,0.55)
        self.car6.setScale(0.2)

        self.car6.reparentTo(self.render)

        self.sq4= Sequence(self.car6.posInterval(20, Point3(-24,-70,0.55), Point3(-24,100,0.55)), self.car6.posInterval(20, Point3(-24,-100,0.55), Point3(-24,-70,0.55)))
        self.sq4.loop()



        self.car7 = self.loader.loadModel('models/car2/scene.gltf')
        self.car7.setPos(-24,-40,0.55)
        self.car7.setScale(0.2)

        self.car7.reparentTo(self.render)

        self.sq5= Sequence(self.car7.posInterval(20, Point3(-24,-40,0.55), Point3(-24,100,0.55)), self.car7.posInterval(20, Point3(-24,-100,0.55), Point3(-24,-40,0.55)))
        self.sq5.loop()



        self.car8 = self.loader.loadModel('models/car2/scene.gltf')
        self.car8.setPos(-24,10,0.55)
        self.car8.setScale(0.2)

        self.car8.reparentTo(self.render)

        self.sq6= Sequence(self.car8.posInterval(20, Point3(-24,10,0.55), Point3(-24,100,0.55)), self.car8.posInterval(20, Point3(-24,-100,0.55), Point3(-24,10,0.55)))
        self.sq6.loop()



        # Set people
        # self.npc1 = self.loader.loadModel('./models/npc3/scene.gltf')
        # self.npc1.setPos(3,-8,0)
        # self.npc1.setScale(0.008)
        # self.npc1.setHpr(self.npc1, -30, 0,0)

        # self.npc1.reparentTo(self.render)

        # self.npc2 = self.loader.loadModel('./models/npc2/scene.gltf')
        # self.npc2.setPos(-3,-15,0)
        # self.npc2.setScale(0.008)
        # self.npc2.setHpr(self.npc2, 30, 90,0)

        # self.npc2.reparentTo(self.render)





        self.moveCar()


    def lightControl(self,  key):
        self.keyMap[key] = not self.keyMap.get(key)

        if key=="0":
            self.cameraModel.setX(0)
            self.cameraModel.setY(-20)
            self.cameraModel.setZ(3)

        if key=="1":
            self.cameraModel.setX(0)
            self.cameraModel.setY(-80)
            self.cameraModel.setZ(40)

        if key=="2":
            self.cameraModel.setX(20)
            self.cameraModel.setY(-10)
            self.cameraModel.setZ(3)

        if key =="c":
            if self.keyMap["c"]:
                self.render.clearLight(self.carLight_r_Np)
                self.render.clearLight(self.carLight_l_Np)
            else:
                self.render.setLight(self.carLight_r_Np)
                self.render.setLight(self.carLight_l_Np)
        elif key =="l":
            if self.keyMap["l"]:
                self.taskMgr.remove("Update Lights")
                self.render.clearLight(self.directionalLightNodePath)
                self.render.setLight(self.moon_NodePath)

            else:
                self.render.setLight(self.directionalLightNodePath)
                self.taskMgr.add(self.updateLights, "Update Lights")
                self.render.clearLight(self.moon_NodePath)
        elif key =="h":
            if self.keyMap["h"]:
                self.render.clearLight(self.house_light_1_NodePath)
                self.render.clearLight(self.house_light_2_NodePath)
                self.render.clearLight(self.house_light_3_NodePath)
            else:
                self.render.setLight(self.house_light_1_NodePath)
                self.render.setLight(self.house_light_2_NodePath)
                self.render.setLight(self.house_light_3_NodePath)
        elif key =="p":
            if self.keyMap["p"]:
                self.render.clearLight(self.lamp_light_1_NodePath)
                self.render.clearLight(self.lamp_light_2_NodePath)
            else:
                self.render.setLight(self.lamp_light_1_NodePath)
                self.render.setLight(self.lamp_light_2_NodePath)
        



    def setKey(self, key, value):
        self.keyMap[key] = value

    def toggle(self, key):
        self.keyMap[key] = not self.keyMap.get(key)


    def cameraControl(self, task):
        
        dt = globalClock.getDt()
        if(dt > .20):
            return task.cont

        if(base.mouseWatcherNode.hasMouse()):
            mpos = base.mouseWatcherNode.getMouse()
            base.camera.setP(mpos.getY() * 30)
            base.camera.setH(mpos.getX() * -50)
            if (mpos.getX() < 0.1 and mpos.getX() > -0.1 ):
                self.cameraModel.setH(self.cameraModel.getH())
            else:
                self.cameraModel.setH(self.cameraModel.getH() + mpos.getX() * -1)

        if(self.keyMap["w"]):
            self.cameraModel.setY(self.cameraModel, 15 * dt)
            return task.cont
        elif(self.keyMap["s"]):
            self.cameraModel.setY(self.cameraModel, -15 * dt)
            return task.cont
        elif(self.keyMap["a"]):
            self.cameraModel.setX(self.cameraModel, -10 * dt)
            return task.cont
        elif(self.keyMap["d"]):
            self.cameraModel.setX(self.cameraModel, 10 * dt)
            return task.cont
        elif(self.keyMap["shift"]):
            self.cameraModel.setZ(self.cameraModel, -10 * dt)
            return task.cont
        elif(self.keyMap["space"]):
            self.cameraModel.setZ(self.cameraModel, 10 * dt)
            return task.cont
        else:
            return task.cont


    def updateLights(self, task):

        if self.mySound.status() != self.mySound.PLAYING:
            self.mySound.play()
        time_speed=0.001
        # Update the time of day
        self.timeOfDay += time_speed
        if self.timeOfDay>2:
            self.timeOfDay=0




        # Update the ambient light
        #self.ambientLight.setColor(self.dayColors[int(self.timeOfDay)])

        # Update the directional light
        if self.timeOfDay < 1:
            # Daytime to Nightime
            self.backgroundColor[0]-=0.7451 * time_speed
            self.backgroundColor[1]-=0.802 * time_speed
            self.backgroundColor[2]-=0.7412 * time_speed
            self.setBackgroundColor(self.backgroundColor)

            self.lightPosition[0]-=0.2*time_speed
            self.lightPosition[1]+=2*time_speed
            self.lightPosition[2]+=0.5*time_speed
            self.directionalLight.setDirection(self.lightPosition)

            if self.timeOfDay<0.5:
                self.lightColor[1]-=0.352*time_speed
                self.lightColor[2]-=1*time_speed
                self.directionalLight.setColor(self.lightColor)
            else:
                self.lightColor[0]-=0.8*time_speed
                self.lightColor[1]-=0.447*time_speed
                self.lightColor[2]+=0.2*time_speed
                self.directionalLight.setColor(self.lightColor)
        elif self.timeOfDay < 2:
            # Nighttime to Daytime
            self.backgroundColor[0]+=0.7451 * time_speed
            self.backgroundColor[1]+=0.802 * time_speed
            self.backgroundColor[2]+=0.7412 * time_speed
            self.setBackgroundColor(self.backgroundColor)


            self.lightPosition[0]+=0.2*time_speed
            self.lightPosition[1]-=2*time_speed
            self.lightPosition[2]-=0.5*time_speed
            self.directionalLight.setDirection(self.lightPosition)

            self.lightColor[0]+=0.8*time_speed
            self.lightColor[1]+=0.8*time_speed
            self.lightColor[2]+=0.8*time_speed
            self.directionalLight.setColor(self.lightColor)

        return Task.cont


    # def spinCameraTask(self, task):

    #     self.cameraRadius = 30.0

    #     angleDegrees = task.time * 60.0

    #     angleRadians = angleDegrees * (pi / 180.0)

    #     self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)

    #     self.camera.setHpr(angleDegrees, 0, 0)

    #     return Task.cont


    #Moving car
    def moveCar(self):
        
        posInterval1 = self.car.posInterval(3,

                                                   Point3(7.0, 7.0, 0.55),

                                                   startPos=Point3(7.0, -6.0, 0.55))

        posInterval2 = self.car.posInterval(3,

                                                   Point3(-7.0, 7.0, 0.55),

                                                   startPos=Point3(7.0, 7.0, 0.55))

        posInterval3 = self.car.posInterval(3,

                                                   Point3(-7.0, -6.0, 0.55),

                                                   startPos=Point3(-7.0, 7.0, 0.55))

        posInterval4 = self.car.posInterval(3,

                                                   Point3(7.0, -6.0, 0.55),

                                                   startPos=Point3(-7.0, -6.0, 0.55))


        hprInterval1 = self.car.hprInterval(3,

                                                   Point3(90, 0, 0),

                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.car.hprInterval(3,

                                                   Point3(180, 0, 0),

                                                   startHpr=Point3(90, 0, 0))
        hprInterval3 = self.car.hprInterval(3,

                                                   Point3(270, 0, 0),

                                                   startHpr=Point3(180, 0, 0))
        hprInterval4 = self.car.hprInterval(3,

                                                   Point3(360, 0, 0),

                                                   startHpr=Point3(270, 0, 0))



        # Create and play the sequence that coordinates the intervals.

        self.carPace = Sequence(posInterval1, hprInterval1,

                                  posInterval2, hprInterval2,

                                  posInterval3, hprInterval3,

                                  posInterval4, hprInterval4,

                                  name="carPace")

        self.carPace.loop()


app = MyApp()

app.run()
