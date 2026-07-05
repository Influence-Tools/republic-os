---
type: Jurisdiction
title: "Wabasha County, MN"
classification: county
fips: "27157"
state: "MN"
demographics:
  population: 21565
  population_under_18: 4706
  population_18_64: 11826
  population_65_plus: 5033
  median_household_income: 82007
  poverty_rate: 7.07
  homeownership_rate: 83.31
  unemployment_rate: 2.21
  median_home_value: 264400
  gini_index: 0.4175
  vacancy_rate: 11.03
  race_white: 20437
  race_black: 90
  race_asian: 154
  race_native: 59
  hispanic: 742
  bachelors_plus: 5506
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/20b"
    rel: in-district
    area_weight: 0.5582
  - to: "us/states/mn/districts/house/20a"
    rel: in-district
    area_weight: 0.4417
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Wabasha County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21565 |
| Under 18 | 4706 |
| 18–64 | 11826 |
| 65+ | 5033 |
| Median household income | 82007 |
| Poverty rate | 7.07 |
| Homeownership rate | 83.31 |
| Unemployment rate | 2.21 |
| Median home value | 264400 |
| Gini index | 0.4175 |
| Vacancy rate | 11.03 |
| White | 20437 |
| Black | 90 |
| Asian | 154 |
| Native | 59 |
| Hispanic/Latino | 742 |
| Bachelor's or higher | 5506 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 20](/us/states/mn/districts/senate/20.md) — 100% (state senate)
- [MN House District 20B](/us/states/mn/districts/house/20b.md) — 56% (state house)
- [MN House District 20A](/us/states/mn/districts/house/20a.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
