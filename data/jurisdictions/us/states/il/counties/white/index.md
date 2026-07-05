---
type: Jurisdiction
title: "White County, IL"
classification: county
fips: "17193"
state: "IL"
demographics:
  population: 13619
  population_under_18: 2957
  population_18_64: 7471
  population_65_plus: 3191
  median_household_income: 54813
  poverty_rate: 16.37
  homeownership_rate: 77.08
  unemployment_rate: 3.96
  median_home_value: 108100
  gini_index: 0.4535
  vacancy_rate: 15.72
  race_white: 13030
  race_black: 78
  race_asian: 35
  race_native: 6
  hispanic: 221
  bachelors_plus: 2426
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9942
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.0058
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.5464
  - to: "us/states/il/districts/house/116"
    rel: in-district
    area_weight: 0.5464
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 0.453
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# White County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13619 |
| Under 18 | 2957 |
| 18–64 | 7471 |
| 65+ | 3191 |
| Median household income | 54813 |
| Poverty rate | 16.37 |
| Homeownership rate | 77.08 |
| Unemployment rate | 3.96 |
| Median home value | 108100 |
| Gini index | 0.4535 |
| Vacancy rate | 15.72 |
| White | 13030 |
| Black | 78 |
| Asian | 35 |
| Native | 6 |
| Hispanic/Latino | 221 |
| Bachelor's or higher | 2426 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 99% (congressional)
- [IN-08](/us/states/in/districts/08.md) — 1% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 55% (state senate)
- [IL House District 116](/us/states/il/districts/house/116.md) — 55% (state house)
- [IL House District 117](/us/states/il/districts/house/117.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
