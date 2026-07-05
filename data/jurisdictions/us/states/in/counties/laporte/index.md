---
type: Jurisdiction
title: "LaPorte County, IN"
classification: county
fips: "18091"
state: "IN"
demographics:
  population: 111917
  population_under_18: 23756
  population_18_64: 66400
  population_65_plus: 21761
  median_household_income: 71055
  poverty_rate: 13.62
  homeownership_rate: 74.75
  unemployment_rate: 4.8
  median_home_value: 195500
  gini_index: 0.4346
  vacancy_rate: 12.8
  race_white: 87406
  race_black: 11828
  race_asian: 715
  race_native: 234
  hispanic: 8498
  bachelors_plus: 24005
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 0.6773
  - to: "us/states/in/districts/01"
    rel: in-district
    area_weight: 0.3079
  - to: "us/states/in/districts/senate/8"
    rel: in-district
    area_weight: 0.8505
  - to: "us/states/in/districts/senate/4"
    rel: in-district
    area_weight: 0.1341
  - to: "us/states/in/districts/house/20"
    rel: in-district
    area_weight: 0.7747
  - to: "us/states/in/districts/house/9"
    rel: in-district
    area_weight: 0.1877
  - to: "us/states/in/districts/house/7"
    rel: in-district
    area_weight: 0.0223
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# LaPorte County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 111917 |
| Under 18 | 23756 |
| 18–64 | 66400 |
| 65+ | 21761 |
| Median household income | 71055 |
| Poverty rate | 13.62 |
| Homeownership rate | 74.75 |
| Unemployment rate | 4.8 |
| Median home value | 195500 |
| Gini index | 0.4346 |
| Vacancy rate | 12.8 |
| White | 87406 |
| Black | 11828 |
| Asian | 715 |
| Native | 234 |
| Hispanic/Latino | 8498 |
| Bachelor's or higher | 24005 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 68% (congressional)
- [IN-01](/us/states/in/districts/01.md) — 31% (congressional)
- [IN Senate District 8](/us/states/in/districts/senate/8.md) — 85% (state senate)
- [IN Senate District 4](/us/states/in/districts/senate/4.md) — 13% (state senate)
- [IN House District 20](/us/states/in/districts/house/20.md) — 77% (state house)
- [IN House District 9](/us/states/in/districts/house/9.md) — 19% (state house)
- [IN House District 7](/us/states/in/districts/house/7.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
