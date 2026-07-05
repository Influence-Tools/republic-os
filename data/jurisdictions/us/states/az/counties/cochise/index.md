---
type: Jurisdiction
title: "Cochise County, AZ"
classification: county
fips: "04003"
state: "AZ"
demographics:
  population: 125773
  population_under_18: 26670
  population_18_64: 38322
  population_65_plus: 60781
  median_household_income: 60723
  poverty_rate: 13.33
  homeownership_rate: 72.71
  unemployment_rate: 5.39
  median_home_value: 231600
  gini_index: 0.4483
  vacancy_rate: 11.39
  race_white: 79312
  race_black: 4768
  race_asian: 2736
  race_native: 1700
  hispanic: 44719
  bachelors_plus: 35041
districts:
  - to: "us/states/az/districts/06"
    rel: in-district
    area_weight: 0.9296
  - to: "us/states/az/districts/07"
    rel: in-district
    area_weight: 0.0704
  - to: "us/states/az/districts/senate/19"
    rel: in-district
    area_weight: 0.9543
  - to: "us/states/az/districts/senate/21"
    rel: in-district
    area_weight: 0.0457
  - to: "us/states/az/districts/house/19"
    rel: in-district
    area_weight: 0.9543
  - to: "us/states/az/districts/house/21"
    rel: in-district
    area_weight: 0.0457
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Cochise County, AZ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 125773 |
| Under 18 | 26670 |
| 18–64 | 38322 |
| 65+ | 60781 |
| Median household income | 60723 |
| Poverty rate | 13.33 |
| Homeownership rate | 72.71 |
| Unemployment rate | 5.39 |
| Median home value | 231600 |
| Gini index | 0.4483 |
| Vacancy rate | 11.39 |
| White | 79312 |
| Black | 4768 |
| Asian | 2736 |
| Native | 1700 |
| Hispanic/Latino | 44719 |
| Bachelor's or higher | 35041 |

## Districts

- [AZ-06](/us/states/az/districts/06.md) — 93% (congressional)
- [AZ-07](/us/states/az/districts/07.md) — 7% (congressional)
- [AZ Senate District 19](/us/states/az/districts/senate/19.md) — 95% (state senate)
- [AZ Senate District 21](/us/states/az/districts/senate/21.md) — 5% (state senate)
- [AZ House District 19](/us/states/az/districts/house/19.md) — 95% (state house)
- [AZ House District 21](/us/states/az/districts/house/21.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
