#!/usr/bin/env python3

import unittest
import rospy
import rostest
from std_srvs.srv import Trigger, TriggerResponse


# class TestMoveAndTurnService:
class TestMoveAndTurnService(unittest.TestCase):
    # def __init__(self):
    def test_start_move_and_turn_service(self):
        # Create the service proxy
        service = rospy.ServiceProxy('start_move_and_turn', Trigger)
        rospy.loginfo(" Llamada a servicio")
        # Call the service and check the response
        response = service()
        self.assertTrue(response.success)
        self.assertEqual(response.message, "Move and Turn Started")
        rospy.loginfo(response.success)
        # Close the service proxy to release resources
        service.close()


if __name__ == '__main__':
    print("Inicializando nodo")
    rospy.init_node('test_move_and_turn_service')
    print("1")
    rospy.wait_for_service('/start_move_and_turn')
    rospy.loginfo("Started move_and_turn node")
    print("2")
    #test = TestMoveAndTurnService()

    # Run the test with rostest
    rostest.rosrun('move_and_turn', 'test_move_and_turn_service',
                   TestMoveAndTurnService)
