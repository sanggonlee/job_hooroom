module Api exposing (PostingsResponse, decodePostingsResponse, decodeTotals)

import Json.Decode exposing (Decoder, map, field, string, int, list)

type alias PostingsResponse =
    {
        total : Int
    --,   hits : List String
    }

decodePostingsResponse : Decoder String
decodePostingsResponse =
    field "total" string
    -- map PostingsResponse
    --     (field "total" int)
    --     --(field "hits" (list string))

decodeTotals : Decoder String
decodeTotals =
    field "hits" string
