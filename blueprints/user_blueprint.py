from collections import Counter

from flask import Blueprint, jsonify
from sqlalchemy.orm import joinedload

from database.PostgreSQL_connection import  session_maker
from database.mongo_db_connection import get_mongo_connection
from models import User, HostageSentence, ExplosiveSentence

user_bp = Blueprint('user', __name__)


@user_bp.route('/api/suspicious_content/<string:email>', methods=['GET'])
def get_info_by_email(email):
    with session_maker() as session:
        user = (
            session.query(User)
            .options(joinedload(User.hostage_sentences), joinedload(User.explosive_sentences))
            .filter_by(email=email)
            .first()
        )
        if not user:
            return jsonify({"message": "User not found"}), 404
        hostage_sentences = [sentence.sentence for sentence in user.hostage_sentences]
        explosive_sentences = [sentence.sentence for sentence in user.explosive_sentences]
    mongo_collection = get_mongo_connection()
    mongo_user = mongo_collection.find_one({"email": email}, {"_id": 0, "sentences": 1})

    if not mongo_user:
        return jsonify({"message": "MongoDB data not found for the user"}), 404

    all_sentences = hostage_sentences + explosive_sentences + mongo_user.get('sentences', [])

    return jsonify({
        "email": email,
        "hostage_sentences": hostage_sentences,
        "explosive_sentences": explosive_sentences,
        "all_sentences": all_sentences
    })

@user_bp.route('/api/most_common_word', methods=['GET'])
def get_most_common_word():
    with session_maker() as session:
        all_sentences = (
            session.query(HostageSentence.sentence)
            .union(session.query(ExplosiveSentence.sentence))
            .all()
        )
        words = [word.lower() for sentence in all_sentences for word in sentence[0].split()]
        word_counts = Counter(words).most_common(1)

        if word_counts:
            most_common_word, frequency = word_counts[0]
            return jsonify({"most_common_word": most_common_word, "frequency": frequency})
        else:
            return jsonify({"message": "No words found"}), 404