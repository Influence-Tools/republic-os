---
type: Jurisdiction
title: "Calumet County, WI"
classification: county
fips: "55015"
state: "WI"
demographics:
  population: 52942
  population_under_18: 11760
  population_18_64: 32078
  population_65_plus: 9104
  median_household_income: 88810
  poverty_rate: 5.88
  homeownership_rate: 80.08
  unemployment_rate: 2.12
  median_home_value: 274200
  gini_index: 0.4002
  vacancy_rate: 4.98
  race_white: 46733
  race_black: 509
  race_asian: 1375
  race_native: 130
  hispanic: 3016
  bachelors_plus: 15692
districts:
  - to: "us/states/wi/districts/08"
    rel: in-district
    area_weight: 0.7758
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 0.2242
  - to: "us/states/wi/districts/senate/1"
    rel: in-district
    area_weight: 0.8048
  - to: "us/states/wi/districts/house/3"
    rel: in-district
    area_weight: 0.8048
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Calumet County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 52942 |
| Under 18 | 11760 |
| 18–64 | 32078 |
| 65+ | 9104 |
| Median household income | 88810 |
| Poverty rate | 5.88 |
| Homeownership rate | 80.08 |
| Unemployment rate | 2.12 |
| Median home value | 274200 |
| Gini index | 0.4002 |
| Vacancy rate | 4.98 |
| White | 46733 |
| Black | 509 |
| Asian | 1375 |
| Native | 130 |
| Hispanic/Latino | 3016 |
| Bachelor's or higher | 15692 |

## Districts

- [WI-08](/us/states/wi/districts/08.md) — 78% (congressional)
- [WI-06](/us/states/wi/districts/06.md) — 22% (congressional)
- [WI Senate District 1](/us/states/wi/districts/senate/1.md) — 80% (state senate)
- [WI House District 3](/us/states/wi/districts/house/3.md) — 80% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
