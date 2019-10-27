using System.Collections;
using System.collections.Generic;
using UnityEngine;

public class StockRoom : MonoBehaviour {

    List<SpriteRenderer> sr;
    List<Sprite> sprites;

    void Start() { 
        while(1) {
            ChangeSprite();
        }
    }
    void ChangeSprite() {
        for (i = 0; i < sr.length(); ++i) {
            sr[i]= GetComponent<SpriteRenderer()>;
            sr[i].sprite = sprites[i]; 
			DateTime tThen = DateTime.Now;
			while (DateTime.Now < tThen+1); //wait one second
        }
    }
    void Update() {

    }
}