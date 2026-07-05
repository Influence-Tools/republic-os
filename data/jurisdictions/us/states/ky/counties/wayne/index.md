---
type: Jurisdiction
title: "Wayne County, KY"
classification: county
fips: "21231"
state: "KY"
demographics:
  population: 19602
  population_under_18: 4007
  population_18_64: 11297
  population_65_plus: 4298
  median_household_income: 45739
  poverty_rate: 24.76
  homeownership_rate: 69.14
  unemployment_rate: 5.75
  median_home_value: 135700
  gini_index: 0.4746
  vacancy_rate: 20.33
  race_white: 18055
  race_black: 239
  race_asian: 6
  race_native: 63
  hispanic: 882
  bachelors_plus: 2802
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/ky/districts/senate/15"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/52"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Wayne County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19602 |
| Under 18 | 4007 |
| 18–64 | 11297 |
| 65+ | 4298 |
| Median household income | 45739 |
| Poverty rate | 24.76 |
| Homeownership rate | 69.14 |
| Unemployment rate | 5.75 |
| Median home value | 135700 |
| Gini index | 0.4746 |
| Vacancy rate | 20.33 |
| White | 18055 |
| Black | 239 |
| Asian | 6 |
| Native | 63 |
| Hispanic/Latino | 882 |
| Bachelor's or higher | 2802 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 15](/us/states/ky/districts/senate/15.md) — 100% (state senate)
- [KY House District 52](/us/states/ky/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
