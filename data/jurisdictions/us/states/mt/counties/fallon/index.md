---
type: Jurisdiction
title: "Fallon County, MT"
classification: county
fips: "30025"
state: "MT"
demographics:
  population: 2760
  population_under_18: 653
  population_18_64: 1493
  population_65_plus: 614
  median_household_income: 76250
  poverty_rate: 11.41
  homeownership_rate: 69.44
  unemployment_rate: 0.0
  median_home_value: 244800
  gini_index: 0.503
  vacancy_rate: 20.57
  race_white: 2545
  race_black: 0
  race_asian: 0
  race_native: 62
  hispanic: 4
  bachelors_plus: 354
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/34"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Fallon County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2760 |
| Under 18 | 653 |
| 18–64 | 1493 |
| 65+ | 614 |
| Median household income | 76250 |
| Poverty rate | 11.41 |
| Homeownership rate | 69.44 |
| Unemployment rate | 0.0 |
| Median home value | 244800 |
| Gini index | 0.503 |
| Vacancy rate | 20.57 |
| White | 2545 |
| Black | 0 |
| Asian | 0 |
| Native | 62 |
| Hispanic/Latino | 4 |
| Bachelor's or higher | 354 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 17](/us/states/mt/districts/senate/17.md) — 100% (state senate)
- [MT House District 34](/us/states/mt/districts/house/34.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
