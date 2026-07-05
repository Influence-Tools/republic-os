---
type: Jurisdiction
title: "Oxford County, ME"
classification: county
fips: "23017"
state: "ME"
demographics:
  population: 59255
  population_under_18: 10452
  population_18_64: 34622
  population_65_plus: 14181
  median_household_income: 60173
  poverty_rate: 13.83
  homeownership_rate: 80.62
  unemployment_rate: 4.29
  median_home_value: 217300
  gini_index: 0.4588
  vacancy_rate: 34.5
  race_white: 55104
  race_black: 201
  race_asian: 386
  race_native: 117
  hispanic: 1002
  bachelors_plus: 14479
districts:
  - to: "us/states/me/districts/02"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/me/districts/senate/19"
    rel: in-district
    area_weight: 0.7659
  - to: "us/states/me/districts/senate/18"
    rel: in-district
    area_weight: 0.2013
  - to: "us/states/me/districts/senate/22"
    rel: in-district
    area_weight: 0.0326
  - to: "us/states/me/districts/house/73"
    rel: in-district
    area_weight: 0.3781
  - to: "us/states/me/districts/house/81"
    rel: in-district
    area_weight: 0.1509
  - to: "us/states/me/districts/house/78"
    rel: in-district
    area_weight: 0.1172
  - to: "us/states/me/districts/house/82"
    rel: in-district
    area_weight: 0.1052
  - to: "us/states/me/districts/house/77"
    rel: in-district
    area_weight: 0.0866
  - to: "us/states/me/districts/house/79"
    rel: in-district
    area_weight: 0.072
  - to: "us/states/me/districts/house/80"
    rel: in-district
    area_weight: 0.0669
  - to: "us/states/me/districts/house/83"
    rel: in-district
    area_weight: 0.0228
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Oxford County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59255 |
| Under 18 | 10452 |
| 18–64 | 34622 |
| 65+ | 14181 |
| Median household income | 60173 |
| Poverty rate | 13.83 |
| Homeownership rate | 80.62 |
| Unemployment rate | 4.29 |
| Median home value | 217300 |
| Gini index | 0.4588 |
| Vacancy rate | 34.5 |
| White | 55104 |
| Black | 201 |
| Asian | 386 |
| Native | 117 |
| Hispanic/Latino | 1002 |
| Bachelor's or higher | 14479 |

## Districts

- [ME-02](/us/states/me/districts/02.md) — 100% (congressional)
- [ME Senate District 19](/us/states/me/districts/senate/19.md) — 77% (state senate)
- [ME Senate District 18](/us/states/me/districts/senate/18.md) — 20% (state senate)
- [ME Senate District 22](/us/states/me/districts/senate/22.md) — 3% (state senate)
- [ME House District 73](/us/states/me/districts/house/73.md) — 38% (state house)
- [ME House District 81](/us/states/me/districts/house/81.md) — 15% (state house)
- [ME House District 78](/us/states/me/districts/house/78.md) — 12% (state house)
- [ME House District 82](/us/states/me/districts/house/82.md) — 11% (state house)
- [ME House District 77](/us/states/me/districts/house/77.md) — 9% (state house)
- [ME House District 79](/us/states/me/districts/house/79.md) — 7% (state house)
- [ME House District 80](/us/states/me/districts/house/80.md) — 7% (state house)
- [ME House District 83](/us/states/me/districts/house/83.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
