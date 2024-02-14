from rest_framework.routers import DefaultRouter

from .viewsets import (
    ChatMediaViewSet,
    ChatMessageReactionsViewSet,
    ChatMessageViewSet,
    ChatRoomViewSet,
    RoomUserViewSet,
)

router = DefaultRouter()

router.register("room", ChatRoomViewSet, basename="room")
router.register("user", RoomUserViewSet, basename="user")
router.register("message", ChatMessageViewSet, basename="message")
router.register("media", ChatMediaViewSet, basename="media")
router.register(
    "message_reactions", ChatMessageReactionsViewSet, basename="message_reactions"
)

urlpatterns = router.urls
