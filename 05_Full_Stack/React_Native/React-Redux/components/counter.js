import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Container, Content, Text, Card, Header, Body, Button, Title, CardItem } from 'native-base';
import { increment, decrement } from '../reducers/countReducer';

class Counter extends Component {
    render() {
    return(
      <Container>
        <Header>
          <Body>
            <Title>Redux Counter</Title>
          </Body>
        </Header>
        <Content padder>
          <Card>
            <CardItem>
              <Text>
                { this.props.state.count }
              </Text>
            </CardItem>
          </Card>
          <Button full onPress= {() => this.props.increment()} style={{marginVertical: 10}}>
            <Text>Increment</Text>
          </Button>
          <Button full dark bordered onPress= {() => this.props.decrement()}>
            <Text>Decrement</Text>
          </Button>
        </Content>
      </Container>
    );
  }
}

// Reducer 데이터를 props로 변환
function mapStateToProps(state){
    return {
      state: state.countReducer
    };
  }
  
// Actions을 props로 변환 :
function matchDispatchToProps(dispatch){
    return bindActionCreators({
        increment: increment,
        decrement: decrement
    }, dispatch);
}
  
export default connect(mapStateToProps, matchDispatchToProps)(Counter);

  