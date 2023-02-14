"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parksapi.models import Photo

class SongView(ViewSet):
    """Tuna API song view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single song

        Returns:
            Response -- JSON serialized song
        """

        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all songs

        Returns:
            Response -- JSON serialized list of songs
        """

        songs = Song.objects.all()

        if "genre" in request.query_params:
            genres = Genre.objects.all()

            for iterator in genres:
                if iterator.id == int(request.query_params['genre']):
                    songs = songs.filter(genre_id=iterator.id)

        if "artist" in request.query_params:
            artists = Artist.objects.all()

            for iterator in artists:
                if iterator.id == int(request.query_params['artist']):
                    songs = songs.filter(artist_id=iterator.id)

        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized song instance
        """

        song = Song.objects.create(
            title=request.data["title"],
            album_name=request.data["album_name"],
            length=request.data["length"],
            genre=Genre.objects.get(pk=request.data["genre"]),
            artist=Artist.objects.get(pk=request.data["artist"])
        )

        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SongGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """

    class Meta:
        model = Genre
        fields = ('description', )

class SongArtistSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """

    class Meta:
        model = Artist
        fields = ('full_name', )

class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """
    genre = SongGenreSerializer()
    artist = SongArtistSerializer()

    class Meta:
        model = Song
        fields = ('id', 'title', 'genre', 'artist', 'album_name', 'length')
