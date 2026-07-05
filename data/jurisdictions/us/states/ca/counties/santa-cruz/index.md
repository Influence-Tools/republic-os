---
type: Jurisdiction
title: "Santa Cruz County, CA"
classification: county
fips: "06087"
state: "CA"
demographics:
  population: 264926
  population_under_18: 48713
  population_18_64: 165938
  population_65_plus: 50275
  median_household_income: 111093
  poverty_rate: 11.62
  homeownership_rate: 59.94
  unemployment_rate: 6.12
  median_home_value: 1027500
  gini_index: 0.4831
  vacancy_rate: 9.42
  race_white: 159010
  race_black: 2200
  race_asian: 12961
  race_native: 3172
  hispanic: 93346
  bachelors_plus: 111904
districts:
  - to: "us/states/ca/districts/19"
    rel: in-district
    area_weight: 0.6597
  - to: "us/states/ca/districts/18"
    rel: in-district
    area_weight: 0.0737
  - to: "us/states/ca/districts/senate/17"
    rel: in-district
    area_weight: 0.7357
  - to: "us/states/ca/districts/house/28"
    rel: in-district
    area_weight: 0.5318
  - to: "us/states/ca/districts/house/29"
    rel: in-district
    area_weight: 0.1175
  - to: "us/states/ca/districts/house/30"
    rel: in-district
    area_weight: 0.0865
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Santa Cruz County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 264926 |
| Under 18 | 48713 |
| 18–64 | 165938 |
| 65+ | 50275 |
| Median household income | 111093 |
| Poverty rate | 11.62 |
| Homeownership rate | 59.94 |
| Unemployment rate | 6.12 |
| Median home value | 1027500 |
| Gini index | 0.4831 |
| Vacancy rate | 9.42 |
| White | 159010 |
| Black | 2200 |
| Asian | 12961 |
| Native | 3172 |
| Hispanic/Latino | 93346 |
| Bachelor's or higher | 111904 |

## Districts

- [CA-19](/us/states/ca/districts/19.md) — 66% (congressional)
- [CA-18](/us/states/ca/districts/18.md) — 7% (congressional)
- [CA Senate District 17](/us/states/ca/districts/senate/17.md) — 74% (state senate)
- [CA House District 28](/us/states/ca/districts/house/28.md) — 53% (state house)
- [CA House District 29](/us/states/ca/districts/house/29.md) — 12% (state house)
- [CA House District 30](/us/states/ca/districts/house/30.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
