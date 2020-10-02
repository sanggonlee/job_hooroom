module Posting exposing (view)

import Html exposing (Html, button, div, text)
import Html.Attributes exposing (style)

-- VIEW

view: String -> Html msg
view description =
  div [ style "padding" "50px" ]
    [ div [] [ text description ]
    ]
