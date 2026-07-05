---
type: Jurisdiction
title: "Lincoln County, KS"
classification: county
fips: "20105"
state: "KS"
demographics:
  population: 2923
  population_under_18: 617
  population_18_64: 1564
  population_65_plus: 742
  median_household_income: 57500
  poverty_rate: 11.34
  homeownership_rate: 80.44
  unemployment_rate: 2.41
  median_home_value: 96900
  gini_index: 0.4342
  vacancy_rate: 23.38
  race_white: 2706
  race_black: 2
  race_asian: 17
  race_native: 5
  hispanic: 133
  bachelors_plus: 753
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/109"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Lincoln County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2923 |
| Under 18 | 617 |
| 18–64 | 1564 |
| 65+ | 742 |
| Median household income | 57500 |
| Poverty rate | 11.34 |
| Homeownership rate | 80.44 |
| Unemployment rate | 2.41 |
| Median home value | 96900 |
| Gini index | 0.4342 |
| Vacancy rate | 23.38 |
| White | 2706 |
| Black | 2 |
| Asian | 17 |
| Native | 5 |
| Hispanic/Latino | 133 |
| Bachelor's or higher | 753 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 109](/us/states/ks/districts/house/109.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
