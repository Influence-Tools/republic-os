---
type: Jurisdiction
title: "Bibb County, AL"
classification: county
fips: "01007"
state: "AL"
demographics:
  population: 22130
  population_under_18: 4437
  population_18_64: 13847
  population_65_plus: 3846
  median_household_income: 52541
  poverty_rate: 22.46
  homeownership_rate: 79.18
  unemployment_rate: 12.08
  median_home_value: 145700
  gini_index: 0.4367
  vacancy_rate: 15.65
  race_white: 16378
  race_black: 4378
  race_asian: 99
  race_native: 130
  hispanic: 766
  bachelors_plus: 2571
districts:
  - to: "us/states/al/districts/06"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/al/districts/senate/14"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/49"
    rel: in-district
    area_weight: 0.6809
  - to: "us/states/al/districts/house/72"
    rel: in-district
    area_weight: 0.3188
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Bibb County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22130 |
| Under 18 | 4437 |
| 18–64 | 13847 |
| 65+ | 3846 |
| Median household income | 52541 |
| Poverty rate | 22.46 |
| Homeownership rate | 79.18 |
| Unemployment rate | 12.08 |
| Median home value | 145700 |
| Gini index | 0.4367 |
| Vacancy rate | 15.65 |
| White | 16378 |
| Black | 4378 |
| Asian | 99 |
| Native | 130 |
| Hispanic/Latino | 766 |
| Bachelor's or higher | 2571 |

## Districts

- [AL-06](/us/states/al/districts/06.md) — 100% (congressional)
- [AL Senate District 14](/us/states/al/districts/senate/14.md) — 100% (state senate)
- [AL House District 49](/us/states/al/districts/house/49.md) — 68% (state house)
- [AL House District 72](/us/states/al/districts/house/72.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
