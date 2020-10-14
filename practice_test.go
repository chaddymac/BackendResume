package main

import (
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"github.com/aws/aws-sdk-go/service/dynamodb/dynamodbiface"
	"testing"
)

// Define stub
type mockDynamoDBClient struct {
	dynamodbiface.DynamoDBAPI
}

func (m *mockDynamoDBClient) GetItem(input *dynamodb.GetItemInput) (*dynamodb.GetItemOutput, error) {
	// Make response
	key := dynamodb.AttributeValue{}
	key.SetS("key")
	val := dynamodb.AttributeValue{}
	val.SetS("counter")
	resp := make(map[string]*dynamodb.AttributeValue)
	resp["key"] = &key
	resp["val"] = &val

	// Returned canned response
	output := &dynamodb.GetItemOutput{
		Item: resp,
	}
	return output, nil
}

// Sample Test Case
func TestDynamodb(t *testing.T) {
	mockSvc := &mockDynamoDBClient{}
	Counter(mockSvc)
}
