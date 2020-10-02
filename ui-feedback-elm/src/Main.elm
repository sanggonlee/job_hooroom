module Main exposing (main, update, view)

import Debug
import Browser
import Html exposing (Html, button, div, text, pre)
import Html.Attributes exposing (style)
import Html.Events exposing (onClick)
import Http

import Api
import Posting

main: Program () Model Msg
main =
  Browser.element
    { init = init
    , update = update
    , subscriptions = subscriptions
    , view = view
    }

-- Model

type Model
  = Failure String
  | Loading
  | Success String

init : () -> (Model, Cmd Msg)
init _ =
    (
        Loading
    ,   Http.get
            {
                url = "https://..."
            ,   expect = Http.expectJson GotResponse Api.decodeTotals
            }
    )

type Msg
    = GotResponse (Result Http.Error String)

update: Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    GotResponse result ->
      case result of
        Ok fullText ->
          (Success fullText, Cmd.none)

        Err e ->
          (Failure (Debug.toString e), Cmd.none)


-- SUBSCRIPTIONS

subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none


-- VIEW

view : Model -> Html Msg
view model =
  case model of
    Failure e ->
      text e

    Loading ->
      text "Loading..."

    Success postings ->
      pre [] [ Posting.view postings ]
