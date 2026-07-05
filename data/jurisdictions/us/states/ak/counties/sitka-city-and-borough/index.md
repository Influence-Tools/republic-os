---
type: Jurisdiction
title: "Sitka City and Borough, AK"
classification: county
fips: "02220"
state: "AK"
demographics:
  population: 8368
  population_under_18: 1766
  population_18_64: 2944
  population_65_plus: 3658
  median_household_income: 101727
  poverty_rate: 7.48
  homeownership_rate: 61.72
  unemployment_rate: 6.78
  median_home_value: 450300
  gini_index: 0.3647
  vacancy_rate: 17.33
  race_white: 4901
  race_black: 42
  race_asian: 720
  race_native: 641
  hispanic: 577
  bachelors_plus: 2901
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.6908
  - to: "us/states/ak/districts/senate/a"
    rel: in-district
    area_weight: 0.6615
  - to: "us/states/ak/districts/house/2"
    rel: in-district
    area_weight: 0.6615
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Sitka City and Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8368 |
| Under 18 | 1766 |
| 18–64 | 2944 |
| 65+ | 3658 |
| Median household income | 101727 |
| Poverty rate | 7.48 |
| Homeownership rate | 61.72 |
| Unemployment rate | 6.78 |
| Median home value | 450300 |
| Gini index | 0.3647 |
| Vacancy rate | 17.33 |
| White | 4901 |
| Black | 42 |
| Asian | 720 |
| Native | 641 |
| Hispanic/Latino | 577 |
| Bachelor's or higher | 2901 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 69% (congressional)
- [AK Senate District A](/us/states/ak/districts/senate/a.md) — 66% (state senate)
- [AK House District 2](/us/states/ak/districts/house/2.md) — 66% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
