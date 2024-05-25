import rclpy
import cv2  
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
from std_msgs.msg import String


class program(Node):
    def __init__(self):
        super().__init__('publisher')
        self.pub_camera = self.create_publisher(Image,'detection',10)
        
        self.time = 0.5
        self.timer = self.create_timer(self.time,self.camera_callback) 
        self.image = cv2.VideoCapture(0) 
        self.face_cascade = cv2.CascadeClassifier('/home/ilknur/ros2_opencv/src/my_package/my_package/facedetection.xml') 
        self.store_bridge = CvBridge()


    #subscrbing to the image camera topic.
    def camera_callback(self):

        while True:
            __ret,frame = self.image.read()
            reading =self.face_cascade.detectMultiScale(frame)
            for (x,y,w,h) in reading:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow("frame",frame)

            
            self.msg = self.store_bridge.cv2_to_imgmsg(frame,"bgr8")
            self.pub_camera.publish(self.msg) 
            self.get_logger().info('Yüzü Tespiti Yapıldı')

            



            #cv2.imshow("frame_name",frame)
            if cv2.waitKey(20) and 0xFF == ord('q'):
                break

        self.image.release()
        #cv2.destroyAllWindows()

            

      
        

def main(args=None):
    rclpy.init(args=args)
    store = program() #passing in an object.
    rclpy.spin(store)


if __name__ == '__main__':
    main()










