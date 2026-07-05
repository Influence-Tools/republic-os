---
type: Jurisdiction
title: "Chilton County, AL"
classification: county
fips: "01021"
state: "AL"
demographics:
  population: 45992
  population_under_18: 11105
  population_18_64: 27085
  population_65_plus: 7802
  median_household_income: 65603
  poverty_rate: 14.02
  homeownership_rate: 76.86
  unemployment_rate: 5.47
  median_home_value: 161300
  gini_index: 0.4236
  vacancy_rate: 9.9
  race_white: 37129
  race_black: 4354
  race_asian: 200
  race_native: 135
  hispanic: 4707
  bachelors_plus: 6966
districts:
  - to: "us/states/al/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/senate/30"
    rel: in-district
    area_weight: 0.5371
  - to: "us/states/al/districts/senate/14"
    rel: in-district
    area_weight: 0.4628
  - to: "us/states/al/districts/house/42"
    rel: in-district
    area_weight: 0.89
  - to: "us/states/al/districts/house/49"
    rel: in-district
    area_weight: 0.1099
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Chilton County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45992 |
| Under 18 | 11105 |
| 18–64 | 27085 |
| 65+ | 7802 |
| Median household income | 65603 |
| Poverty rate | 14.02 |
| Homeownership rate | 76.86 |
| Unemployment rate | 5.47 |
| Median home value | 161300 |
| Gini index | 0.4236 |
| Vacancy rate | 9.9 |
| White | 37129 |
| Black | 4354 |
| Asian | 200 |
| Native | 135 |
| Hispanic/Latino | 4707 |
| Bachelor's or higher | 6966 |

## Districts

- [AL-06](/us/states/al/districts/06.md) — 100% (congressional)
- [AL Senate District 30](/us/states/al/districts/senate/30.md) — 54% (state senate)
- [AL Senate District 14](/us/states/al/districts/senate/14.md) — 46% (state senate)
- [AL House District 42](/us/states/al/districts/house/42.md) — 89% (state house)
- [AL House District 49](/us/states/al/districts/house/49.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
