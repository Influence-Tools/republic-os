---
type: Jurisdiction
title: "Lawrence County, IL"
classification: county
fips: "17101"
state: "IL"
demographics:
  population: 15031
  population_under_18: 2796
  population_18_64: 9456
  population_65_plus: 2779
  median_household_income: 55324
  poverty_rate: 14.49
  homeownership_rate: 71.84
  unemployment_rate: 8.1
  median_home_value: 99100
  gini_index: 0.4286
  vacancy_rate: 14.59
  race_white: 12621
  race_black: 932
  race_asian: 69
  race_native: 7
  hispanic: 323
  bachelors_plus: 2237
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.995
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.005
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Lawrence County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15031 |
| Under 18 | 2796 |
| 18–64 | 9456 |
| 65+ | 2779 |
| Median household income | 55324 |
| Poverty rate | 14.49 |
| Homeownership rate | 71.84 |
| Unemployment rate | 8.1 |
| Median home value | 99100 |
| Gini index | 0.4286 |
| Vacancy rate | 14.59 |
| White | 12621 |
| Black | 932 |
| Asian | 69 |
| Native | 7 |
| Hispanic/Latino | 323 |
| Bachelor's or higher | 2237 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IN-08](/us/states/in/districts/08.md) — 0% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 100% (state senate)
- [IL House District 102](/us/states/il/districts/house/102.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
