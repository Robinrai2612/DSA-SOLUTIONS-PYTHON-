//{ Driver Code Starts
//

#include <bits/stdc++.h> 
using namespace std; 

struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};


void printList(Node* node) 
{ 
	while (node != NULL) { 
		cout << node->data <<" "; 
		node = node->next; 
	}  
	cout<<"\n";
}

// } Driver Code Ends

class Solution{
  public:
        Node *sortedInsert(struct Node* head, int data) {
        if(data < head->data)
        {
            Node*newNode = new Node(data);
            newNode->next = head;
            head = newNode;
            return head;
        }
        Node*temp = head;
        Node*prev = NULL;
        while(temp!= NULL and temp->data <= data)
        {
           prev = temp;
           temp = temp->next;
        }
        Node* newNode = new Node(data);
        newNode->next = temp;
        prev->next = newNode;
        return head;
      // Code here
    }
};


//{ Driver Code Starts.
int main() 
{ 
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
        
		int data;
		cin>>data;
		
		struct Node *head = new Node(data);
		struct Node *tail = head;
		for (int i = 0; i < n-1; ++i)
		{
			cin>>data;
			tail->next = new Node(data);
			tail = tail->next;
		}
		
		int k;
		cin>>k;
		Solution obj;
		head = obj.sortedInsert(head,k);
		printList(head); 
	}
	return 0; 
} 

// } Driver Code Ends