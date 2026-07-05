---
type: Jurisdiction
title: "Spencer County, IN"
classification: county
fips: "18147"
state: "IN"
demographics:
  population: 19955
  population_under_18: 4313
  population_18_64: 11526
  population_65_plus: 4116
  median_household_income: 74506
  poverty_rate: 7.47
  homeownership_rate: 81.34
  unemployment_rate: 3.33
  median_home_value: 185200
  gini_index: 0.3936
  vacancy_rate: 7.44
  race_white: 18688
  race_black: 113
  race_asian: 49
  race_native: 31
  hispanic: 721
  bachelors_plus: 4319
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/in/districts/senate/48"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/in/districts/house/74"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Spencer County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19955 |
| Under 18 | 4313 |
| 18–64 | 11526 |
| 65+ | 4116 |
| Median household income | 74506 |
| Poverty rate | 7.47 |
| Homeownership rate | 81.34 |
| Unemployment rate | 3.33 |
| Median home value | 185200 |
| Gini index | 0.3936 |
| Vacancy rate | 7.44 |
| White | 18688 |
| Black | 113 |
| Asian | 49 |
| Native | 31 |
| Hispanic/Latino | 721 |
| Bachelor's or higher | 4319 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 48](/us/states/in/districts/senate/48.md) — 100% (state senate)
- [IN House District 74](/us/states/in/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
