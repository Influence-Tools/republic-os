---
type: Jurisdiction
title: "Charlotte County, FL"
classification: county
fips: "12015"
state: "FL"
demographics:
  population: 201064
  population_under_18: 26652
  population_18_64: 38634
  population_65_plus: 135778
  median_household_income: 69952
  poverty_rate: 8.99
  homeownership_rate: 83.8
  unemployment_rate: 5.37
  median_home_value: 328900
  gini_index: 0.4479
  vacancy_rate: 23.71
  race_white: 167048
  race_black: 10406
  race_asian: 2737
  race_native: 184
  hispanic: 16501
  bachelors_plus: 63250
districts:
  - to: "us/states/fl/districts/17"
    rel: in-district
    area_weight: 0.7862
  - to: "us/states/fl/districts/senate/27"
    rel: in-district
    area_weight: 0.7838
  - to: "us/states/fl/districts/house/76"
    rel: in-district
    area_weight: 0.5907
  - to: "us/states/fl/districts/house/75"
    rel: in-district
    area_weight: 0.1931
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Charlotte County, FL

County jurisdiction — 21 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 201064 |
| Under 18 | 26652 |
| 18–64 | 38634 |
| 65+ | 135778 |
| Median household income | 69952 |
| Poverty rate | 8.99 |
| Homeownership rate | 83.8 |
| Unemployment rate | 5.37 |
| Median home value | 328900 |
| Gini index | 0.4479 |
| Vacancy rate | 23.71 |
| White | 167048 |
| Black | 10406 |
| Asian | 2737 |
| Native | 184 |
| Hispanic/Latino | 16501 |
| Bachelor's or higher | 63250 |

## Districts

- [FL-17](/us/states/fl/districts/17.md) — 79% (congressional)
- [FL Senate District 27](/us/states/fl/districts/senate/27.md) — 78% (state senate)
- [FL House District 76](/us/states/fl/districts/house/76.md) — 59% (state house)
- [FL House District 75](/us/states/fl/districts/house/75.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
