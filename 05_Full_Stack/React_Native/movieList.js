// movieList.js
import React, {Component} from 'react';
import {FlatList, Text, View, ActivityIndicator, StyleSheet} from 'react-native';

export default class MovieList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoaded: false,
            title: "",
            description: "",
            movieList: []
        };
    }

    componentDidMount() {
        this.fetchMovies();
    }

    fetchMovies = async () => {
        try {
            const response = await fetch('https://facebook.github.io/react-native/movies.json');
            const responseJson = await response.json();
            this.setState({
                isLoaded: true,
                title: responseJson.title,
                description: responseJson.description,
                movieList: responseJson.movies
            });
            console.log("Loading complete");
        } catch (error) {
            console.error(error);
        }
    };

    render() {
        const {isLoaded, movieList} = this.state;

        return (
            <View style={styles.container}>
                <Text style={styles.header}>영화목록 가져오기</Text>
                {isLoaded ? (
                    <FlatList
                        data={movieList}
                        keyExtractor={(item, index) => index.toString()}
                        renderItem={({item}) => (
                            <Text style={styles.movieItem}>
                                {item.title} ({item.releaseYear})
                            </Text>
                        )}
                    />
                ) : (
                    <ActivityIndicator size="large" color="#0000ff" />
                )}
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16,
        backgroundColor: '#fff',
    },
    header: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 16,
    },
    movieItem: {
        fontSize: 16,
        marginVertical: 8,
    },
});