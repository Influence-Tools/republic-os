---
type: Jurisdiction
title: "Portsmouth city, VA"
classification: county
fips: "51740"
state: "VA"
demographics:
  population: 97190
  population_under_18: 24424
  population_18_64: 35850
  population_65_plus: 36916
  median_household_income: 60491
  poverty_rate: 17.34
  homeownership_rate: 57.94
  unemployment_rate: 6.55
  median_home_value: 246900
  gini_index: 0.4494
  vacancy_rate: 6.99
  race_white: 35186
  race_black: 49167
  race_asian: 1673
  race_native: 299
  hispanic: 5225
  bachelors_plus: 21912
districts:
  - to: "us/states/va/districts/03"
    rel: in-district
    area_weight: 0.8408
  - to: "us/states/va/districts/senate/18"
    rel: in-district
    area_weight: 0.4965
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 0.2664
  - to: "us/states/va/districts/house/88"
    rel: in-district
    area_weight: 0.6851
  - to: "us/states/va/districts/house/91"
    rel: in-district
    area_weight: 0.0772
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Portsmouth city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 97190 |
| Under 18 | 24424 |
| 18–64 | 35850 |
| 65+ | 36916 |
| Median household income | 60491 |
| Poverty rate | 17.34 |
| Homeownership rate | 57.94 |
| Unemployment rate | 6.55 |
| Median home value | 246900 |
| Gini index | 0.4494 |
| Vacancy rate | 6.99 |
| White | 35186 |
| Black | 49167 |
| Asian | 1673 |
| Native | 299 |
| Hispanic/Latino | 5225 |
| Bachelor's or higher | 21912 |

## Districts

- [VA-03](/us/states/va/districts/03.md) — 84% (congressional)
- [VA Senate District 18](/us/states/va/districts/senate/18.md) — 50% (state senate)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 27% (state senate)
- [VA House District 88](/us/states/va/districts/house/88.md) — 69% (state house)
- [VA House District 91](/us/states/va/districts/house/91.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
