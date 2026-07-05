---
type: Jurisdiction
title: "Macoupin County, IL"
classification: county
fips: "17117"
state: "IL"
demographics:
  population: 44350
  population_under_18: 9136
  population_18_64: 25648
  population_65_plus: 9566
  median_household_income: 70805
  poverty_rate: 13.06
  homeownership_rate: 78.49
  unemployment_rate: 3.67
  median_home_value: 138200
  gini_index: 0.4311
  vacancy_rate: 16.86
  race_white: 41656
  race_black: 654
  race_asian: 130
  race_native: 50
  hispanic: 608
  bachelors_plus: 8493
districts:
  - to: "us/states/il/districts/13"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 0.5005
  - to: "us/states/il/districts/senate/54"
    rel: in-district
    area_weight: 0.4995
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 0.5005
  - to: "us/states/il/districts/house/108"
    rel: in-district
    area_weight: 0.4995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Macoupin County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44350 |
| Under 18 | 9136 |
| 18–64 | 25648 |
| 65+ | 9566 |
| Median household income | 70805 |
| Poverty rate | 13.06 |
| Homeownership rate | 78.49 |
| Unemployment rate | 3.67 |
| Median home value | 138200 |
| Gini index | 0.4311 |
| Vacancy rate | 16.86 |
| White | 41656 |
| Black | 654 |
| Asian | 130 |
| Native | 50 |
| Hispanic/Latino | 608 |
| Bachelor's or higher | 8493 |

## Districts

- [IL-13](/us/states/il/districts/13.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 50% (state senate)
- [IL Senate District 54](/us/states/il/districts/senate/54.md) — 50% (state senate)
- [IL House District 100](/us/states/il/districts/house/100.md) — 50% (state house)
- [IL House District 108](/us/states/il/districts/house/108.md) — 50% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
