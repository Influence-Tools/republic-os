---
type: Jurisdiction
title: "Salem city, VA"
classification: county
fips: "51775"
state: "VA"
demographics:
  population: 25618
  population_under_18: 6050
  population_18_64: 8294
  population_65_plus: 11274
  median_household_income: 66725
  poverty_rate: 10.25
  homeownership_rate: 62.8
  unemployment_rate: 3.6
  median_home_value: 258600
  gini_index: 0.4631
  vacancy_rate: 7.7
  race_white: 21128
  race_black: 2217
  race_asian: 503
  race_native: 67
  hispanic: 1227
  bachelors_plus: 7985
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9951
  - to: "us/states/va/districts/senate/4"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/va/districts/house/40"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Salem city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25618 |
| Under 18 | 6050 |
| 18–64 | 8294 |
| 65+ | 11274 |
| Median household income | 66725 |
| Poverty rate | 10.25 |
| Homeownership rate | 62.8 |
| Unemployment rate | 3.6 |
| Median home value | 258600 |
| Gini index | 0.4631 |
| Vacancy rate | 7.7 |
| White | 21128 |
| Black | 2217 |
| Asian | 503 |
| Native | 67 |
| Hispanic/Latino | 1227 |
| Bachelor's or higher | 7985 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 4](/us/states/va/districts/senate/4.md) — 100% (state senate)
- [VA House District 40](/us/states/va/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
