from src.entities.agents.Agent import Agent
from src.utils.Menus import Menus
__author__ = 'ezequiel'


class AgentController():
    """
    Agent Controller class
    This controller is the responsible of options like listing, creating or deleting agents
    """

    def __init__(self):
        """
        Init function
        This method instantiate a AgentController class object

        :return: Instance of AgentController
        """

        pass

    @staticmethod
    def agent_controller(org):
        """
        Agent controller method:
        It's the class main method. It provides with the functions that will allow the application managing agents

        :param org: Current organization
        """

        menu_back = False
        while not menu_back:
            option = Menus.agent_menu()
            if option == 1:
                AgentController.list_agents(org)
            elif option == 2:
                AgentController.create_agent(org)
            elif option == 3:
                AgentController.remove_agent(org)
            elif option == 0:
                menu_back = True

    @staticmethod
    def list_agents(org):
        """
        List agents method
        Responsible of displaying a list of agents that belong to the organization

        :param org: Organization
        """
        for agent in org.agent_list:
            print "-"*30
            print agent

    @staticmethod
    def create_agent(org):
        """
        Create agent method
        This function aims to create a new agent and add it to the organization's agent list

        :param org: Organization
        """

        a_id = raw_input("Agent ID: ")
        firstname = raw_input("First name: ")
        lastname = raw_input("Last name: ")
        birthdate = raw_input("Birth date name: ")
        email = raw_input("e-Mail: ")
        base = float(raw_input("Base: "))
        a = Agent(a_id, firstname, lastname, birthdate, base, email)
        org.addAgent(a)
        print "The agent with ID " + a.agent_id + "has been successfully created and added to the company"

    @staticmethod
    def remove_agent(org):
        """
        Remove agent method
        Removes an agent from the organization's agent list

        :param org: Organization
        """

        i = 1
        for agent in org.agent_list:
            print "-"*30
            print "#"+str(i) + " - First name: "+agent.firstname+" Last name" + agent.lastname + " ID: "+agent.agent_id
            i += 1
        selection = 0
        while selection < 1 or selection > i:
            selection = int(raw_input("Select the agent to be deleted: "))
        org.agent_list.pop(selection-1)