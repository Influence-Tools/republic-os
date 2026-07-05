---
type: Jurisdiction
title: "Humboldt County, NV"
classification: county
fips: "32013"
state: "NV"
demographics:
  population: 17289
  population_under_18: 4562
  population_18_64: 9868
  population_65_plus: 2859
  median_household_income: 81073
  poverty_rate: 10.63
  homeownership_rate: 73.97
  unemployment_rate: 5.78
  median_home_value: 278300
  gini_index: 0.3914
  vacancy_rate: 11.03
  race_white: 11831
  race_black: 143
  race_asian: 265
  race_native: 553
  hispanic: 4720
  bachelors_plus: 2708
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/senate/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/house/32"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Humboldt County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17289 |
| Under 18 | 4562 |
| 18–64 | 9868 |
| 65+ | 2859 |
| Median household income | 81073 |
| Poverty rate | 10.63 |
| Homeownership rate | 73.97 |
| Unemployment rate | 5.78 |
| Median home value | 278300 |
| Gini index | 0.3914 |
| Vacancy rate | 11.03 |
| White | 11831 |
| Black | 143 |
| Asian | 265 |
| Native | 553 |
| Hispanic/Latino | 4720 |
| Bachelor's or higher | 2708 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 100% (congressional)
- [NV Senate District 14](/us/states/nv/districts/senate/14.md) — 100% (state senate)
- [NV House District 32](/us/states/nv/districts/house/32.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
